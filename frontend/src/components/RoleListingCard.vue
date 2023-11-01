<template>
  <v-card v-if="!loading" class="ma-6" max-width="95%" color="primary">
    {{ isRepeatApplication }}
    {{ id }}
    {{ this.userID }}
    <v-card-item>
      <div>
        <div class="text-overline mb-1">Department: {{ department }}</div>
        <div class="text-h6 mb-1">{{ name }}</div>
        <div class="text-caption">
          {{ description }}
        </div>

        <v-item-group class="d-flex justify-space-between align-center">
          <v-item>
            <v-chip label class="ma-0">Expires: {{ expiry }}</v-chip>
          </v-item>

          <v-card-actions>
            <v-btn v-if="match !== 0 && !isRepeatApplication" variant="outlined" @click="applyForRole"> Apply </v-btn>
            <v-btn v-else variant="outlined" disabled> Apply </v-btn>
          </v-card-actions>
        </v-item-group>

        <v-item-group>
          <v-item v-if="skillsGap.length != 0">
            <b>Missing Skills:</b>
            <div v-for="skill in skillsGap">
              {{ skill }}
            </div>
          </v-item>

          <v-item v-else>
            Your suit the role perfectly!
          </v-item>
        </v-item-group>
        
          <v-progress-linear v-if="match !== null" v-model="match"  color="blue-lighten-3" height="25" rounded>
          <template v-slot:default="{ value }">
            <strong>{{value}}% Skills Match</strong>
          </template>
        </v-progress-linear>
        
      </div>
    </v-card-item>
  </v-card>
</template>

<script>
import axios from 'axios';
import { useAppStore } from '@/store/app';
export default {
  data() {
    return{
      match: Math.round(this.matchPercentage * 100),
      skillsGap: this.missingSkills,
      userID: null,
      isRepeatApplication: null,
      loading: true
    }
  },
  props: ["id", "name", "description", "expiry", "department", "matchPercentage","missingSkills"],

  async mounted() {
    const store = useAppStore();
    this.userID = store.getCurrentUserID;
    this.isRepeatApplication = await this.isApplicationSubmitted();
    if (this.isRepeatApplication !== null) {
      this.loading = false;
    }
  },
  methods: {
    async applyForRole() {
      const roleID = this.id;
      try {
        const response = await axios.post(`http://localhost:5001/apply/${this.userID}/${roleID}`);
        console.log(response);
        if (response.status === 200) {
          alert(response.data);
        }
        else {
          alert(response.data);
        }
      } catch (error) {
        console.log(error);
        alert("Failed to apply for role!");
      }
    },
    async isApplicationSubmitted() {
      const roleID = this.id;
      try {
        const response = await axios.get(`http://localhost:5001/getAllRoleApplications`);
        if (response.status === 200) {
          for (let i = 0; i < response.data.length; i++) {
            if (parseInt(response.data[i][0]) == parseInt(roleID) && parseInt(response.data[i][1]) == parseInt(this.userID)) {
              return true;
            }
          }
            return false;        
        }
        else {
          return false;
        }
      } catch (error) {
        console.log("Error:" + error);
        return false;
      }
    }
  }
};
</script>
