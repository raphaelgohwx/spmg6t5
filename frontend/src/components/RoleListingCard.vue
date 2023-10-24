<template>
  <v-card class="ma-6" max-width="95%" color="primary">
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
            <v-btn v-if="match !== 0" variant="outlined" @click="applyForRole"> Apply </v-btn>
            <v-btn v-else variant="outlined" disabled> Apply </v-btn>
          </v-card-actions>
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
    }
  },
  props: ["id", "name", "description", "expiry", "department", "matchPercentage"],
  methods: {
    async applyForRole () {
      const store = useAppStore();
      const userID = store.getCurrentUserID;
      const roleID = this.id;
      try {
        const response = await axios.post(`http://localhost:5001/api/apply/${userID}/${roleID}`);
        console.log(response);
        // if (response.status === 200) {
        //   alert("Successfully applied for role!");
        // }
        // else {
        //   alert("Failed to apply for role!");
        // }
      } catch (error) {
        console.log(error);
      }
    }
  }
};
</script>
