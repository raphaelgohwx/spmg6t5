<template>
  <div>
    <navbar />
    <p v-if="store.getCurrentUser == null" class="text-center text-h4">Please Log In to Access</p>

    <div v-if="store.getCurrentUser == 'Manager' || store.getCurrentUser == 'HR'">
      <div class="text-center text-h4">
        Welcome {{ store.getCurrentUser }}
      </div>
            <div v-if="this.staff_roles.length != 0">
        <template v-for="role in staff_roles">
          <RoleListingCardforManager
            :name="role.Role_Name"
            :description="role.Role_Description"
            :expiry="role.Date_Closed.substr(0, 16)"
            :department="role.Dept"
          />
        </template>
      </div>

    <div v-else>There are currently no role listings</div>
  </div>


  <div v-if="store.getCurrentUser == 'Staff'">
      <div class="text-center text-h4">
        Welcome {{ store.getCurrentUser }}
      </div>
      <div v-if="this.staff_roles.length != 0">
        <div class="filter">
            <div>
              <div class="filter-button">
              <button @click="toggleFilterOptions"> Select Filter </button>  
              </div>
              <div v-if="showFilterOptions">   
                
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
                <option v-for="dept in depts" :key="dept" :value="dept">{{ dept }}</option>
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
              <input type="date" id="closingDateFilter" v-model="closingDateFilter" @input="setMinDate" />
            </div>
            <!-- Need to disable all previous dates -->
            
      
            <div v-if="selectFilter != null" class="resetter">
              <!-- Reset button to clear filters -->
              <button @click="clearFilters">Reset Filter</button>
            </div>
          </div> 
          </div>
        </div>

        <!-- Display filtered roles -->
        <div v-if="filteredRoles.length > 0">
          <p>Filtered listings shown below. </p>
          <template v-for="role in filteredRoles">
            <RoleListingCard
              :name="role.Role_Name"
              :description="role.Role_Description"
              :expiry="role.Date_Closed.substr(0, 16)"
              :department="role.Dept"
            />
          </template>
        </div>

        <div v-else>
          <div v-if="selectFilter != null">
            <b> No role listings found within filter. </b>
          </div>
          <div v-else>
            <p> No filters applied.</p>
          </div>
          <p> All role listings shown below.</p>
          <div>
          <template v-for="role in staff_roles">
            <RoleListingCard
              :name="role.Role_Name"
              :description="role.Role_Description"
              :expiry="role.Date_Closed.substr(0, 16)"
              :department="role.Dept"
            />
          </template>
        </div>
        </div>
      </div>
        
      <div v-else>
        There are currently no role listings.
      </div>
    </div>
  </div>
</template>

<script>
import navbar from "@/components/navbar.vue";
import RoleListingCardforManager from "@/components/RoleListingCardforManager.vue";
import RoleListingCard from "@/components/RoleListingCard.vue";
import ApiService from "@/store/api_service";
import { useAppStore } from "@/store/app";
import axios from 'axios';

export default {
  data() {
    return {
      staff_roles: [],
      selectFilter: null,
      deptFilter: null,
      skillFilter: null,
      closingDateFilter: null,
      depts: [],
      skills: ["Attention to Detail",
                  "Stakeholder Management",
                  "Communication",
                  "Analytical Skills",
                  "Teamwork",
                  "Adaptability",
                  "Creative Thinking",
                  "Project Management",
                  "Coding",
                  "Critical Thinking",
                  "Data Analytics"
                ],
      filteredRoles: [],
      showFilterOptions: false, // Initially hide filter options
    };
  },
  setup() {
    const store = useAppStore();
    console.log(store.getCurrentUser)
    return { store };
  },
  components: {
    navbar,
    RoleListingCard,
    RoleListingCardforManager,
  },
  created() {
    ApiService.getActiveRoleListings().then((res) => {
      this.staff_roles = res.data;
      console.log(this.staff_roles); 
      
    });
  },
  mounted() {
    this.getDeptNames();
  },
  methods: {
    async getDeptNames() {
      const response = await axios.get('http://localhost:5001/getDeptNames');
      this.depts = response.data;
    },

    async filterRoleListingsBySkill() {
        try {
          if (this.skillFilter) {
            const response = await axios.get('http://localhost:5001/filterRoleListingsBySkill/' + this.skillFilter);
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
          const response = await axios.get('http://localhost:5001/filterRoleListingsByDept/' + this.deptFilter);
          this.filteredRoles = response.data;
        } else {
          this.filteredRoles = [];
        }
      } catch (error) {
        console.error("Error filtering roles by dept:", error);
      }
    },
    async filterRoleListingsByEndDate(){
      try {
        if (this.closingDateFilter) {
          const response = await axios.get('http://localhost:5001/filterRoleListingsByEndDate/' + this.closingDateFilter);
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
    const month = (today.getMonth() + 1).toString().padStart(2, '0'); // Adding 1 to month as it's 0-based
    const day = today.getDate().toString().padStart(2, '0');
    const minDate = `${year}-${month}-${day}`;
    document.getElementById('closingDateFilter').min = minDate;
    },

    clearFilters() {
      this.deptFilter = null;
      this.closingDateFilter = null;
      this.skillFilter = null;
      this.selectFilter = null;
      this.showFilterOptions = false;
    },
    toggleFilterOptions() {
      this.showFilterOptions = !this.showFilterOptions;
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

.resetter button{
  background-color: #6C757D;
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
</style>
