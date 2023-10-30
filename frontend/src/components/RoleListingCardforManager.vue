<template>
  <v-card class="ma-6" max-width="95%" color="primary">
    <v-card-item>
      <div>
        <div class="text-overline mb-1">Department: {{ department }}</div>
        <div class="text-h6 mb-1">{{ name }}</div>
        <div class="text-caption">
          {{ description }}
        </div>
        <div>
          <v-chip label class="ma-0">Expires: {{ expiry }}</v-chip>
        </div>
        <v-item-group class="d-flex pa-2 justify-end">
          <!-- Button to update role listing -->

            <v-btn variant="outlined" to="/UpdateRole">Update Role</v-btn>
            <v-btn variant="outlined"> Apply </v-btn>
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

        <v-progress-linear
          v-if="match !== null"
          v-model="match"
          color="blue-lighten-3"
          height="25"
          rounded
        >
          <template v-slot:default="{ value }">
            <strong>{{ value }}% Skills Match</strong>
          </template>
        </v-progress-linear>
      </div>
    </v-card-item>

    <v-divider></v-divider>

    <v-expansion-panels>
      <v-expansion-panel title="Applicants" expand-icon="mdi-account-group">
        <v-expansion-panel-text>
          <v-row v-for="applicant in Applicants">
            <v-col cols="4">{{ applicant.name }}</v-col>
            <v-col cols="4">{{ applicant.score }}%</v-col>
            <v-col cols="4">
              <v-expansion-panels>
                <v-expansion-panel title="Skills">
                  <v-expansion-panel-text>
                    <v-row class="mt-2">
                      <v-col cols="12" v-for="skill in applicant.skills">{{
                        skill
                      }}</v-col>
                    </v-row>
                  </v-expansion-panel-text>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-col>
          </v-row>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      // Applicants should follow this format
      // Applicants: [
      //   {
      //     name: "Applicant 1",
      //     skills: ["Skill 1", "Skill 2"],
      //     score: 50,
      //   },
      //   {
      //     name: "Applicant 2",
      //     skills: ["Skill 1", "Skill 2", "Skill 3"],
      //     score: 75,
      //   },
      // ],
      match: Math.round(this.matchPercentage * 100),
      skillsGap: this.missingSkills,
    };
  },
  props: ["name", "description", "expiry", "department", "matchPercentage","missingSkills"],
};
</script>

<!-- <style>
.rolebtn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  margin: 10px 10px;
}

.rolebtn:hover {
  background-color: #0056b3; /* darker when you hover over it */
}
</style> -->
