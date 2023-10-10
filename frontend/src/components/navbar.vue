<template>
  <v-card>
    <!-- Header and symbols -->
    <v-toolbar color="primary">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>LJPS</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-text-field
        dense
        variant="solo"
        label="Search"
        append-inner-icon="mdi-magnify"
        single-line
        hide-details
      ></v-text-field>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>

      <!-- Nav bar extensions -->
      <template v-slot:extension>
        <v-tabs v-model="tab" align-tabs="title">
          <v-tab v-for="(item, index) in items" :key="index" :value="index">
            {{ item.label }}
          </v-tab>
        </v-tabs>

        <!-- Login button -->
        <v-spacer></v-spacer>
        <v-menu transition="slide-y-transition">
          <template v-slot:activator="{ props }">
            <v-btn
              v-bind="props"
              :style="{
                marginRight: 30 + 'px',
                backgroundColor: '#28359',
                color: 'white',
              }"
              @click="getAllStaffName()"
            >
              Login
            </v-btn>
          </template>
          <v-list v-model="username">
            <template v-for="staff in staff_list">
              <!-- List item onclick to state -->
              <v-list-item @click="navigateToRole(staff[2])">{{ staff[0] + " " + staff[1]}} | {{ staff[2] }}</v-list-item>
            </template>
            
            <!-- <v-list-item @click="navigateToRole('staff')">Staff</v-list-item>
            <v-list-item @click="navigateToRole('hr')">HR</v-list-item>
            <v-list-item @click="navigateToRole('manager')"
              >Manager</v-list-item
            > -->

          </v-list>
        </v-menu>
      </template>
    </v-toolbar>
  </v-card>
</template>

<script>
import { useAppStore } from "@/store/app";
import ApiService from "@/store/api_service";

export default {
  setup() {
    const appStore = useAppStore();
    return { appStore };
  },
  data() {
    return {
      username: "",
      staff_list: [],
      tab: null,
      items: [
        { label: "Learning Journeys" },
        { label: "Skills" },
        { label: "Courses" },
        { label: "Jobs" },
      ],
    };
  },
  methods: {
    handleItemClick(item) {
      console.log("Clicked item: ${item.title}");
    },
    // async getAllStaffRole(){
    //   await this.appStore.getStaffRoles()
    // },
    navigateToRole(role) {
      this.appStore.saveResponsetoStore(role);
      // this.$router.push({ name: role.toLowerCase() });
    },
    getAllStaffName() {
      ApiService.getAllStaffName().then((res) => {
        this.staff_list = res.data;
      });
    },
  },
  created() {},
};
</script>
