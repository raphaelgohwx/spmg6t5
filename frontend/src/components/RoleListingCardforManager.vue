<template>
    <v-card class="ma-6" max-width="95%" color="primary">
        <v-card-item>
            <div>
                <div class="text-overline mb-1">Department: {{ department }}</div>
                <div class="text-h6 mb-1">{{ name }}</div>
                <div class="text-caption">
                {{ description }}
                </div>
                <v-item-group class="d-flex justify-space-between">
                <v-item>
                    <v-chip label class="ma-0">Expires: {{ expiry }}</v-chip>
                </v-item>
                <!-- Button to update role listing -->
                <RouterLink to="/UpdateRole"><button class="rolebtn">Update Role</button></RouterLink>
                </v-item-group>
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
                                    <v-col cols="12" v-for="skill in applicant.skills">{{ skill }}</v-col>
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
        Applicants: [
            {
                name: "Applicant 1",
                skills: ["Skill 1", "Skill 2"],
                score: 50,
            },
            {
                name: "Applicant 2",
                skills: ["Skill 1", "Skill 2", "Skill 3"],
                score: 75,
            },
        ]
      };
    },
    props: ["name", "description", "expiry", "department"],
  };
  </script>

<style>
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
</style>
  