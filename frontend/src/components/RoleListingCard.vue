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
            <v-btn variant="outlined"> Apply </v-btn>
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

export default {
  data() {
    return{
      match: Math.round(this.matchPercentage * 100)
    }
  },
  props: ["name", "description", "expiry", "department", "matchPercentage"],
};
</script>
