<template>
    <div>
      <navbar />
    </div>
    <div>
      <h2>Update Role Listing</h2>
      <form @submit.prevent="updateRoleListing">
        <div class="form-group">
          <label for="roleName">Role Name:</label>
          <input type="text" id="roleName" v-model="roleName" required />
        </div>
        <div class="form-group">
          <label for="roleDescription">Description:</label>
          <input type="text" id="roleDescription" v-model="roleDescription" required />
        </div>
        <div class="form-group">
          <label for="department">Department:</label>
          <input type="text" id="department" v-model="department" required />
        </div>
        <div class="form-group">
          <label for="closingDate">Closing Date:</label>
          <input type="date" id="closingDate" v-model="closingDate" required />
        </div>
        <button type="submit" class="btn btn-primary">Update Role Listing</button>
      </form>
      <!-- Testing -->
      <v-btn @click='getAllUpdatedListings()'>Test updated listings</v-btn>
    </div>
  </template>
  
  <script>
  import navbar from '@/components/navbar.vue';
  import axios from 'axios';
  
  export default {
    components: {
      navbar,
    },
    data() {
      return {
        //fetch existing role listing data
        roleName: "",        
        roleDescription: "",   
        department: "",      
        closingDate: "",
      };
    },
    mounted() {
      // Fetch existing role listing data from the backend
      this.fetchRoleListingData();
    },
    methods: {
      async fetchRoleListingData() {
        //API request to fetch the existing role listing data
        try {
          const response = await axios.get('http://localhost:5001/getRoleListing');
          const roleListingData = response.data;
  
          // Update data properties with the fetched role listing data
          this.roleName = roleListingData.name;
          this.requiredSkill = roleListingData.skillRequired;
          this.department = roleListingData.department;
          this.closingDate = roleListingData.closingDate;
        } catch (error) {
          console.error("Error fetching role listing data:", error);
        }
      },
      async updateRoleListing() {
        // Create an object with updated role listing data
        const updatedRoleListing = {
          name: this.roleName,
          skillRequired: this.requiredSkill,
          department: this.department,
          closingDate: this.closingDate,
        };
  
        // Send updated data to backend to update role listing
        try {
          const response = await axios.put('http://localhost:5001/updateRoleListing', updatedRoleListing); 
          if (response.status === 200) {
            alert("Role listing updated successfully!");
          } else {
            alert("Failed to update role listing");
          }
        } catch (error) {
            console.error("Error updating role listing:", error);
            alert("Failed to update role listing");
        }
        // Clear the form fields
        this.roleName = "";
        this.requiredSkill = "";
        this.department = "";
        this.closingDate = "";
      },

      
      checkIfRoleListingUpdated() {
        //need connect to backend to see
      }
    },
  };
  </script>
  
<style scoped>
  h2{
  margin-top: 10px;
  margin-bottom: 20px;
  margin-left: 10px;
}

.form-group {
  margin-bottom: 15px;
  margin-left: 10px;

}

label {
  display: block;
  font-weight: bold;
}

input[type="text"] {
  width: 30%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary {
  background-color: #007bff; 
}

.btn-primary:hover {
  background-color: #0056b3; 
  /* darker when you hover over it */
}
</style>
  