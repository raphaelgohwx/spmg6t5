<template>
  <div>
    <navbar />
    <!-- {{ skillMatch }} -->
    <p v-if="store.getCurrentUser == null" class="text-center text-h4">
      Please Log In to Access
    </p>

    <div
      v-if="store.getCurrentUser == 'Manager' || store.getCurrentUser == 'HR'"
    >
      <!-- {{ this.roleListingData }} -->
      <div class="text-center text-h4">Welcome {{ store.getCurrentUser }}</div>
      <div v-if="store.getCurrentUser == 'HR'" > 
        <RouterLink to="/RoleCreation"> <v-btn class="rolebtn">Create a Role Listing</v-btn></RouterLink>
      </div>
      <div v-if="this.staff_roles.length != 0 && this.roleListingData != null">
        <template v-for="role in staff_roles">
          <RoleListingCardforManager
            :id="role.Role_Listing_ID"
            :name="role.Role_Name"
            :description="role.Role_Description"
            :expiry="role.Date_Closed.substr(0, 16)"
            :department="role.Dept"
            :roleListingData="roleListingData[role.Role_Listing_ID]"
          />
        </template>
      </div>

      <div v-else>There are currently no role listings</div>
    </div>

    <div v-if="store.getCurrentUser == 'Staff'">
      <div class="text-center text-h4">Welcome {{ store.getCurrentUser }}</div>
      <div v-if="this.staff_roles.length != 0">

        <div class="filter">
             
            <div>
              <select clearable id="selectFilter" v-model="selectFilter">
                <option :value="null" disabled selected>Filter By</option>
                <option value="Fdept">Department</option>
                <option value="Fskill">Skill</option>
                <option value="Fdate">Closing Date</option>
              </select>
            </div>

              <div v-if="selectFilter == 'Fdept'">
                <!-- Filter by department -->
                <label for="deptFilter">Department:</label>
                <select clearable id="deptFilter" v-model="deptFilter">
                  <option :value="null" disabled selected>Select Dept</option>
                  <option v-for="dept in depts" :key="dept" :value="dept">
                    {{ dept }}
                  </option>
                </select>
              </div>

            <div v-if="selectFilter == 'Fskill'">
              <!-- Filter by skill -->
              <label for="skillFilter">Skill:</label>
              <select clearable id="skillFilter" v-model="skillFilter">
                <option :value="null" disabled selected>Select Skill</option>
                <option v-for="skill in skills" :key="skill" :value="skill">{{ skill }}</option>
              </select>
            </div>
          
            <div v-if="selectFilter == 'Fdate'">
              <!-- Filter by closing date -->
              <label for="closingDateFilter">Closing Date Before:</label>
              <input type="date" id="closingDateFilter" v-model="closingDateFilter" :min="minDate"/>
            </div>
            
      
            <div v-if="selectFilter != null" class="resetter">
              <!-- Reset button to clear filters -->
              <button @click="clearFilters">Reset Filter</button>
            </div>

        </div>

        <!-- Display filtered roles -->
        <div v-if="filteredRoles.length > 0">
          <p>Filtered listings shown below.</p>
          <template v-for="role in filteredRoles">
            <RoleListingCard
              :id="role.Role_Listing_ID"
              :name="role.Role_Name"
              :description="role.Role_Description"
              :expiry="role.Date_Closed.substr(0, 16)"
              :department="role.Dept"
              :matchPercentage="skillMatch[role.Role_Listing_ID][0]"
              :missingSkills="skillMatch[role.Role_Listing_ID][1]"

            />
          </template>
        </div>

          <div v-if="selectFilter != null && filteredRoles.length == 0">
            <div v-if="deptFilter == null && skillFilter == null && closingDateFilter == null">
              <!-- <b> Please select an option from the dropdown to view listings. </b> -->
            </div>
            <div v-else>
              <b> There is no role listing that matches the filter criteria. </b>
            </div>
          </div>

        <!-- Show all role listings -->
        <div v-if="selectFilter == null">

          <template v-if="skillMatch != null && staff_roles != []">
            <template v-for="(role, index) in staff_roles" :key="index">
              <RoleListingCard
                :id="role.Role_Listing_ID"
                :name="role.Role_Name"
                :description="role.Role_Description"
                :expiry="role.Date_Closed.substr(0, 16)"
                :department="role.Dept"
                :matchPercentage="skillMatch[role.Role_Listing_ID][0]"
                :missingSkills="skillMatch[role.Role_Listing_ID][1]"
              />
            </template>
          </template>
            
        </div>

      </div>

      <div v-else>There are currently no role listings.</div>
    </div>
    
  </div>
</template>

<script>
import navbar from "@/components/navbar.vue";
import RoleListingCardforManager from "@/components/RoleListingCardforManager.vue";
import RoleListingCard from "@/components/RoleListingCard.vue";
import ApiService from "@/store/api_service";
import { useAppStore } from "@/store/app";
import axios from "axios";
import {watch, onMounted,onUnmounted, ref } from 'vue'
import { onBeforeMount } from "vue";


export default {
  data() {
    return {
      staff_roles: [],
      displayed_roles: [],
      skillMatch: null,
      finished: false,
      selectFilter: null,
      deptFilter: null,
      skillFilter: null,
      closingDateFilter: null,
      depts: [
        "IT",
        "Sales",
        "Consultancy",
        "HR and Admin",
        "Finance",
        "Engineering Operation Division"
      ],
      skills: [
        "Attention to Detail",
        "Stakeholder Management",
        "Communication",
        "Analytical Skills",
        "Teamwork",
        "Adaptability",
        "Creative Thinking",
        "Project Management",
        "Coding",
        "Critical Thinking",
        "Data Analytics",
      ],
      filteredRoles: [],
      minDate: '',
      roleListingData: null
    };
  },
  setup() {
    const store = useAppStore();
    // console.log(store.getCurrentUser);
    var skillMatch = ref(null);

    onMounted(() => {
      watch(() => store.getCurrentUserID, () => {
        axios.get(`http://localhost:5001/roleSkillMatch/${store.getCurrentUserID}`)
        .then((res) => 
          skillMatch.value = res.data
        )
        .catch((err) => {
          console.log(err)
        });
      })
    })

    return { store,skillMatch };
  },
  components: {
    navbar,
    RoleListingCard,
    RoleListingCardforManager,
  },
  mounted() {
    // const getDeptNames = async() => {
    //     try {
    //       const response = await axios.get("http://localhost:5001/getDeptNames");
    //       this.depts = response.data;
    //     }
    //     catch (error) {
    //       console.log(error)
    //     }
    //   }

    //   getDeptNames();

    
  },

  beforeCreate() {
      // const fetchRoleSkillMatchData = async () => {
      // try {
      //   const response = await axios.get("http://localhost:5001/roleSkillMatch/all");
      //   console.log(response.data)
      //   this.roleListingData = response.data
      // } catch (error) {
      //   console.log(error);
      // }
      // };

      // // Call the async function
      // fetchRoleSkillMatchData();

    //   const getActiveRoleListings = async () => {
    //   try {
    //     const response = await axios.get("http://localhost:5001/getActiveRoleListings");
    //     this.roleListingData = response.data
    //     console.log(this.roleListingData)
    //   } catch (error) {
    //     console.log(error);
    //   }
    //   };

    // getActiveRoleListings();

    axios.get("http://localhost:5001/getActiveRoleListings")
    .then((res) => {
      this.staff_roles = res.data;

      axios.get("http://localhost:5001/roleSkillMatch/all")
      .then((res) => {
        this.roleListingData = res.data;
      })
      .catch((err) => console.log(err))
    })
    .catch((err) => console.log(err))
  },
  created() {
    // ApiService.getActiveRoleListings()
    // .then((res) => {
    //   this.staff_roles = res.data;
    // })
    // .catch((err) => console.log(err));
    // axios.all([
    //   axios.get("http://localhost:5001/getActiveRoleListings"),
    //   axios.get("http://localhost:5001/roleSkillMatch/all")
    // ])
    // .then(axios.spread((response1, response2) => {
    //   this.staff_roles=response1
    //   this.roleListingData=response2
    // }))
    // .catch((err) => console.log(err))
    
  },
  methods: {
    // async getDeptNames() {
    //   const response = await axios.get("http://localhost:5001/getDeptNames");
    //   this.depts = response.data;
    // },

    async filterRoleListingsBySkill() {
      try {
        if (this.skillFilter) {
          const response = await axios.get(
            "http://localhost:5001/filterRoleListingsBySkill/" +
              this.skillFilter
          );
          this.filteredRoles = response.data;
        } else {
          this.filteredRoles = [];
        }
      } catch (error) {
        console.error("Error filtering roles by skill:", error);
      }
    },
    async filterRoleListingsByDept() {
      try {
        if (this.deptFilter) {
          const response = await axios.get(
            "http://localhost:5001/filterRoleListingsByDept/" + this.deptFilter
          );
          this.filteredRoles = response.data;
        } else {
          this.filteredRoles = [];
        }
      } catch (error) {
        console.error("Error filtering roles by dept:", error);
      }
    },
    async filterRoleListingsByEndDate() {
      try {
        if (this.closingDateFilter) {
          const response = await axios.get(
            "http://localhost:5001/filterRoleListingsByEndDate/" +
              this.closingDateFilter
          );
          this.filteredRoles = response.data;
        } else {
          this.filteredRoles = [];
        }
      } catch (error) {
        console.error("Error filtering roles by end date:", error);
      }
    },
    setMinDate() {
      const today = new Date();
      const year = today.getFullYear();
      const month = (today.getMonth() + 1).toString().padStart(2, '0'); // Adding 1 to month as it starts from 0
      const day = today.getDate().toString().padStart(2, '0');
      const todayDate = `${year}-${month}-${day}`;
      this.minDate = todayDate;
    },

    clearFilters() {
      this.deptFilter = null;
      this.closingDateFilter = null;
      this.skillFilter = null;
      this.selectFilter = null;
    },

  },
  watch: {
    skillFilter: "filterRoleListingsBySkill",
    deptFilter: "filterRoleListingsByDept",
    closingDateFilter: "filterRoleListingsByEndDate",
  },
};
</script>

<style scoped>
.filter {
  padding: 10px;
}

.filter label {
  margin-right: 10px;
}

.filter select {
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.resetter button {
  background-color: #6c757d;
  color: #fff;
  border-radius: 10px;
  padding: 5px 10px;
  cursor: pointer;
  margin-right: 10px;
  transition: background-color 0.3s;
}

.filter-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px; /* You can adjust this width */
  border-radius: 4px;
  cursor: pointer;
  margin-left: 10px;
  display: inline-block; /* Added to make it inline */
}

.rolebtn {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: block;
  margin-left: auto;
  margin-right: 20px;
}

.rolebtn:hover {
  background-color: #0056b3; 
  /* darker when you hover over it */
}

</style>
