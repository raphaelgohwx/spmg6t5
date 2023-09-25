<template>
  <div>
    <navbar/>
  </div>

  <div v-if="this.staff_roles.length != 0" >
    <template v-for="role in staff_roles" >
      <RoleListingCard
        :name=" role.Role_Name "
        :description=" role.Role_Description "
        :expiry=" role.Date_Closed.substr(0,16) "
      />
    </template>
  </div>

  <div v-else>
    There are currently no role listings
  </div>
</template>

<script>
import navbar from '@/components/navbar.vue';
import RoleListingCard from '@/components/RoleListingCard.vue';
import ApiService from "@/store/api_service";

export default {
  data() {
    return {
      staff_roles: [],
    }
  },  
  components: {
    navbar,
    RoleListingCard
  },
  created() {
    ApiService.getStaffRoles()
    .then(res => {
      this.staff_roles = res.data
    })
  }
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>