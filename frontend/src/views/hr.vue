<template>
    <div>
      <navbar />
      <p>Welcome Hr</p>
    </div>
    <div>
      <input v-model="roleId" placeholder="Role ID" />
      <br>
      <input v-model="roleName" placeholder="Role Name" />
      <br>
      <input v-model="dateClosed" placeholder="Date Closed" />
      <br>
      <input v-model="description" placeholder="Role Description" />
      <br>
      <input v-model="department" placeholder="Department" />
      <br>
      <v-btn @click='createListing()'>Create Listing</v-btn>
      <v-btn @click='getAllListings()'>Test get all listings</v-btn>
    </div>
  </template>
  
  <script>
  import navbar from '@/components/navbar.vue';
  import roleListingCard from '@/components/RoleListingCard.vue';
  import axios from 'axios';

  
  export default {
    data() {
      return {
        roleId: '',
        roleName: 'Test',
        dateClosed: '12-12-2023 00:03:44',
        description: 'Test',
        department: 'Test'

      };

    },
    components: {
      navbar, roleListingCard
    },
    methods : {
      // async createListing() {
      //   const res = await axios.post('http://localhost:5001/createListing', {
      //     Role_Listing_ID: parseInt(this.roleId),
      //     Role_Name: this.roleName,
      //     Date_Closed: this.dateClosed,
      //     Role_Description: this.description,
      //     Dept: this.department
      //   }, {
      //     headers: {
      //       'Content-Type': 'application/json'

      //     }
      //   })
      //   .then(function (response) {
      //     console.log(response);
      //   })
      //   .catch(function (error) {
      //     console.log(error);
      //   });
        
      // },

      // async getAllListings() {
      //   const res = await axios.get('http://localhost:5001/getAllRoleListings')
      //   console.log(res.data) 
      // }

    }
    
  };

  </script>
 
  
  
  
  
  