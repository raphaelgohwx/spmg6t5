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
        <template v-for="role in staff_roles">
          <RoleListingCard
            :name="role.Role_Name"
            :description="role.Role_Description"
            :expiry="role.Date_Closed.substr(0, 16)"
            :department="role.Dept"
          />
        </template>
      </div>

    <div v-else>There are currently no role listings</div>
  </div>
  </div>

  
</template>

<script>
import navbar from "@/components/navbar.vue";
import RoleListingCardforManager from "@/components/RoleListingCardforManager.vue";
import RoleListingCard from "@/components/RoleListingCard.vue";
import ApiService from "@/store/api_service";
import { useAppStore } from "@/store/app";

export default {
  data() {
    return {
      staff_roles: [],
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
};
</script>

<style scoped></style>
