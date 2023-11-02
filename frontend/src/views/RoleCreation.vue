<template>
    <div>
      <navbar/>
    </div>
      <div>
      <h2>Create New Role Listing</h2>
      <form @submit.prevent="addRoleListing" class="role-listing-form">
        <div class="form-group">
          <label for="roleName">Role Name:</label>
            <select id="roleName" v-model="roleName" required>
              <option :value="null" disabled selected>Select Role</option>
              <option v-for="role in roles" :key="role" :value="role">{{ role }}</option>
            </select>
            <span v-if="roleName.length == 0" class="error">
              Note: Please select a role name.
            </span>
        </div>
        <div class="form-group">
          <label for="roleDescription">Description:</label>
          <textarea id="roleDescription" v-model="roleDescription" required @input="resizeTextarea" />
            <span v-if="roleDescription.length === 0" class="error">
              Note: Description must be between 1 and 100 characters.
            </span>
            <span v-if="roleDescription.length > 100" class="error">
              Note: Description cannot be more than 100 characters long.
            </span>
        </div>
        <div class="form-group">
          <label for="department">Department:</label>
            <select id="department" v-model="department" required>
              <option :value="null" disabled selected>Select Dept</option>
              <option v-for="dept in depts" :key="dept" :value="dept">{{ dept }}</option>
            </select>
            <span v-if="department.length == 0" class="error">
              Note: Please select a department.
            </span>
        </div>
        <div class="form-group">
          <label for="closingDate">Closing Date:</label>
          <input type="date" id="closingDate" v-model="closingDate" required />
          <span v-if="!this.closingDateValidation()" class="error">
              Note: Please select a closing date in the future.
            </span>
        </div>
        <button type="submit" class="btn btn-primary" :disabled="formValidation()">Create Role Listing</button>   
      </form>
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
        roleName: "",
        roleDescription: "",
        department: "",
        closingDate: "",
        roles: ["Account Manager",
                "Admin Team",
                "Call Centre",
                "Consultant",
                "Developer",
                "Finance Executive",
                "Finance Manager",
                "HR Team",
                "IT Team",
                "Junior Engineer",
                "L&D Team",
                "Operation Planning T",
                "Sales Manager",
                "Senior Engineer",
                "Support Team"],
        // depts: [],
        depts: [
        "IT",
        "Sales",
        "Consultancy",
        "HR and Admin",
        "Finance",
        "Engineering Operation Division"
      ],
      };
    },
    mounted() {
    // Page title
    document.title = "Create New Role Listing";

    /// If the backend connection is up, I can get all role names from the backend instead of hardcoding them for the dept dropdown
    /// Once it is, just uncomment the following lines 85 and 107-116, and change the data above to roles: [] 
    // this.getAllRoleNames(); 

    // get all role departments for dropdown
    // this.getAllRoleDepts();
    },
    
    methods: {
      // For visuals only
      resizeTextarea() {
        const textarea = document.getElementById('roleDescription');
        textarea.style.height = 'auto'; // Reset the height to auto to calculate the actual content height
        textarea.style.height = textarea.scrollHeight + 'px'; // Set the height to match the content height
      },

      // checking if selected closingDate is in the future
    closingDateValidation(){
        const dateToday = new Date();
        const dateSelected = new Date(this.closingDate);
        return dateToday <= dateSelected;
      },

      // checking if any of the fields have error, to prevent form submission, hasErrors is true if any of the fields have error
      formValidation() {
        const hasErrors = this.roleName.length === 0 || this.roleDescription.length > 100 || this.roleDescription.length === 0 || this.department.length === 0 || !this.closingDateValidation();
        return hasErrors;
      },
      
      // async getAllRoleNames(){
      //   try {
      //     const response = await axios.get('http://localhost:5001/getRoleNames')
      //     this.roles = response.data;
      //     console.log("Axios Response:", response); // Log the entire response
      //     console.log("All roles:", this.roles);
      //   } catch (error) {
      //     console.error("Error getting all roles:", error);
      //   }
      // },
      
      async getAllRoleDepts(){
        try {
          const response = await axios.get('http://localhost:5001/getDeptNames')
          this.depts = response.data;
          // console.log("All departments:", this.depts);
        } catch (error) {
          console.error("Error getting all departments:", error);
        }
      },

       async addRoleListing() {

          // Create a new role listing object
          const newRoleListing = {
            // Role_Listing_ID: roleListingId, // this is created in app.py
            Role_Name: this.roleName,
            Role_Description: this.roleDescription,
            Dept: this.department,
            Date_Closed: this.closingDate,
          };

          console.log("New Role Listing:", newRoleListing);
          
          try {
          // Make a POST request to your Flask backend to create the role listing
              const response = await axios.post('http://localhost:5001/createRoleListing', newRoleListing)
              console.log(response)
          // Handle the response here, you can show a success message or handle errors
          if (response.data == "Success") {
            alert("Role listing created successfully!");
            this.$router.push('/');
          } else {
            alert("Failed to create role listing");
              }
        } catch (error) {
          console.error("Error creating role listing:", error);
          alert("Failed to create role listing");
        }

      // Clear the form fields
      this.roleName = "";
      this.roleDescription = "";
      this.department = "";
      this.closingDate = "";
      },

      // deleted checkIfRoleListingExists() function because logic is in app.py (backend)
      // deleted async getAllListings() method because logic is in app.py (backend), just run http://localhost:5001/getAllRoleListings in browser to get all listings
      // deleted checkIfRoleListingExists() function because logic is in app.py (backend)
    },
  };

  
</script>

<style scoped>

h2{
  margin-top: 10px;
  margin-bottom: 15px;
  text-align:center;
}

.role-listing-form {
  max-width: 800px; 
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
  width: 40%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
select {
  width: 40%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

input[type="date"]{
  width: 40%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
textarea {
  width: 40%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  height:auto; 
  resize: none; /* Allow vertical resizing */
  overflow-y: hidden; /* Hide vertical scrollbar */
}

.btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  margin-left: 10px;
}

.btn-primary {
  background-color: #007bff; 
}

.btn-primary:hover {
  background-color: #0056b3; 
  /* darker when you hover over it */
}

.error{
  color: #0056b3; 
}
</style>