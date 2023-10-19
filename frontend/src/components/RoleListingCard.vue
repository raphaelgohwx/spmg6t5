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
      </div>
    </v-card-item>
  </v-card>
</template>

<script>
export default {
  props: ["name", "description", "expiry", "department"],
};
</script>
