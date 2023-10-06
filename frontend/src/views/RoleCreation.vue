<template>
    <div>
      <navbar/>
    </div>
      <div>
      <h2>Create New Role Listing</h2>
      <form @submit.prevent="addRoleListing">
        <div class="form-group">
          <label for="roleName">Role Name:</label>
          <input type="text" id="roleName" v-model="roleName" required />
        </div>
        <!-- <div class="form-group">
          <label for="requiredSkill">Skill Required:</label>
          <input type="text" id="requiredSkill" v-model="requiredSkill" required />
        </div> -->
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
        <button type="submit" class="btn btn-primary">Create Role Listing</button>    
      </form>
      <v-btn @click='getAllListings()'>Test get all listings</v-btn>
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
        // need to generate a rolelisting ID, currently the msql id is not auto incrementing so we create on our own
        roleName: "",
        //requiredSkill: "",
        roleDescription: "",
        department: "",
        closingDate: "",
      };
    },
    mounted() {
    // Page title
    document.title = "Create New Role Listing";
    },
    methods: {
       async addRoleListing() {
          // Check if the role listing already exists
          if (this.checkIfRoleListingExists()) {
            alert("Role listing already exists!");
            return;
          }

          const roleListingId = 99; // need to generate automatically
          // Create a new role listing object
          const newRoleListing = {
            Role_Listing_ID: roleListingId,
            Role_Name: this.roleName,
            // skillRequired: this.requiredSkill,
            Role_Description: this.roleDescription,
            Dept: this.department,
            Date_Closed: this.closingDate,
          };

    
          ///// need to connect to backend /////
          // Need to send newRoleListing to the backend
          console.log("New Role Listing:", newRoleListing);
          
          try {
      // Make a POST request to your Flask backend to create the role listing
          const response = await axios.post('http://localhost:5001/createRoleListing', newRoleListing
          )
      // Handle the response here, you can show a success message or handle errors
      if (response.status === 200) {
        alert("Role listing created successfully!");
      } else {
        alert("Failed to create role listing");
          }
        } catch (error) {
          console.error("Error creating role listing:", error);
          alert("Failed to create role listing");
        }

      // Clear the form fields
      this.roleName = "";
      this.requiredSkill = "";
      this.department = "";
      this.closingDate = "";
      },

      checkIfRoleListingExists() {
        ///// need to connect to backend ///// //Alr done in app.py (backend)
        // Check with backend if the role listing already exists
        const existingRoleListings = [
          // Example role listings from the backend
          {
            name: "Developer",
            skillRequired: "Programming",
            department: "Engineering",
            closingDate: "2023-10-04",

          },
          {
            name: "Designer",
            skillRequired: "Graphic Design",
            department: "Creative",
            closingDate: "07-08-2023",
          },
        ];
  
        ///// need to connect to backend /////
        return existingRoleListings.some(
          (listing) =>
            listing.name === this.roleName &&
            listing.requiredSkill === this.requiredSkill &&
            listing.department === this.department &&
            listing.closingDate === this.closingDate
        );
      },

      async getAllListings() {
          const response = await axios.get('http://localhost:5001/getAllRoleListings');
          console.log(response.data);
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
.role-listing-form {
  max-width: 400px; 
  margin: 0 auto; /* Center the form horizontally */
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;

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