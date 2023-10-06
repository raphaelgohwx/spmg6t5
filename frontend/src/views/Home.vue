<template>
  <div>
  <navbar/>
  <p>Please Log In to Access</p>
  </div>

  <div v-if="this.staff_roles.length != 0" >
    <template v-for="role in staff_roles" >
      <RoleListingCard
        :name=" role.Role_Name "
        :description=" role.Role_Description "
        :expiry=" role.Date_Closed.substr(0,16) "
        :department="role.Dept"
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
    ApiService.getActiveRoleListings()
    .then(res => {
      this.staff_roles = res.data
      console.log(this.staff_roles)
    })
  }
};
</script>

<style scoped>
</style>