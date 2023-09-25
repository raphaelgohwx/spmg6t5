<template>
  <v-card class="ma-6" max-width="95%" color="primary" >
    <v-card-item>
      <div>
        <div class="text-overline mb-1">{{ name }}</div>
        <div class="text-h6 mb-1">{{ description }}</div>
        <div class="text-caption">
          {{ expiry }}
        </div>
      </div>
    </v-card-item>

    <v-card-actions>
      <v-btn variant="outlined"> Apply </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
    props: ["name","description","expiry"]
}
</script>
