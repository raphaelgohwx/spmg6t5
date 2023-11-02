<template>
    <div>
      <navbar />
    </div>
    <div>
      <h2>Update Role Listing</h2>
      <form @submit.prevent="updateRoleListing" class="role-listing-form">
        <div class="form-group">
          <label for="listingID">Listing ID:</label>
          <v-text-field id="listingID" v-model="listingID" required>
              <!-- <option :value="null" disabled selected>Select Role</option>
              <option v-for="listing in listingIDList" :key="listing" :value="listing">{{ listing }}</option> -->
            </v-text-field>
        </div>

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
          <textarea id="roleDescription" v-model="roleDescription" required 
          @input="resizeTextarea" />
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
          <v-text-field type="date" v-model="closingDate" required />
          <span v-if="!this.closingDateValidation()" class="error">
              Note: Please select a closing date in the future.
            </span>
        </div>
        <button type="submit" class="btn btn-primary" :disabled="formValidation()">Update Role Listing</button>
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
        //fetch existing role listing data
        listingID: this.$route.params.id,
        listingIDList: "",
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
        depts: ["IT",
                "Sales",
                "Consultancy",
                "Finance",
                "HR and Admin",
                "Engineering Operation Division"],
      };
    },
    mounted() {
      console.log("Listing ID:", this.listingID);
      // Access the id route parameter
      this.listingID = this.$route.params.id;
      // Fetch existing role listing data from the backend
      this.fetchRoleListingData();

    },
    methods: {
      formattedDate(dateInput){
        // change and return date input to YYYY-MM-DD format
        const date = new Date(dateInput);
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        const formattedDate = `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day}`;
        return formattedDate;
      },
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

      async fetchRoleListingData() {
        //API request to fetch the existing role listing data

        // try {
        //   const response = await axios.get('http://localhost:5001/getAllRoleListingIds');
        //   const roleListingData = response.data;
        //   this.listingIDList = roleListingData
        if(this.listingID) {
          try {
            const response = await axios.get(`http://localhost:5001/selectRoleListingByID/${this.listingID}`);
            console.log(this.listingID)
            const roleListingData = response.data;
            console.log(roleListingData)
            // this.listingIDList = roleListingData
            this.listingID = roleListingData[0];
            this.roleName = roleListingData[1];
            this.roleDescription = roleListingData[3];
            this.department = roleListingData[4];
            this.closingDate = this.formattedDate(roleListingData[2]);
            console.log(closingDate)
          
        } catch (error) {
          console.error("Error fetching role listing data:", error);
        }
      }
    },

      async updateRoleListing() {
        // Create an object with updated role listing data
        const updatedRoleListing = {
          Role_Listing_ID: this.listingID,
          Role_Name: this.roleName,
          Role_Description: this.roleDescription,
          Dept: this.department,
          Date_Closed: this.closingDate,
        };
  
        // Send updated data to backend to update role listing
        try {
          const response = await axios.put('http://localhost:5001/updateRoleListing', updatedRoleListing); 
          if (response.status === 200) {
            alert("Role listing updated successfully!");
            this.$router.push('/Home');
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
  