<template>
    <div>
      <navbar/>
    </div>
      <div>
      <h2>Create New Role Listing</h2>
      <form @submit.prevent="addRoleListing" class="role-listing-form">
        <div class="form-group">
          <label for="roleName">Role Name:</label>
          <input type="text" id="roleName" v-model="roleName" required />
            <span v-if="roleName.length > 20 || roleName.length === 0" class="error">
              Note: Role Name must be between 1 and 20 characters.
            </span>
        </div>
        <div class="form-group">
          <label for="roleDescription">Description:</label>
          <textarea id="roleDescription" v-model="roleDescription" required @input="resizeTextarea" />
            <span v-if="roleDescription.length > 100 || roleDescription.length === 0" class="error">
              Note: Description must be between 1 and 100 characters.
            </span>
        </div>
        <div class="form-group">
          <label for="department">Department:</label>
            <select id="department" v-model="department" required>
              <option :value="null" disabled selected>Select Dept</option>

              <!-- Add more departments here if there's changes in database -->
              <option value="IT">IT</option>
              <option value="Sales">Sales</option>
              <option value="Consultancy">Consultancy</option>
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
        <button type="submit" class="btn btn-primary">Create Role Listing</button>    
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
      };
    },
    mounted() {
    // Page title
    document.title = "Create New Role Listing";
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