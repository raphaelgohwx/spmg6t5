<template>
  <v-card>
    <!-- Header and symbols -->
    <v-toolbar color="primary">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>LJPS</v-toolbar-title>

      <v-spacer></v-spacer>

      <!-- <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn> -->

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
        <v-tabs
          v-model="tab"
          align-tabs="title"
        >
          <v-tab
            v-for="(item,index) in items"
            :key="index"
            :value="index"
          >
            {{ item.label }}
          </v-tab>
        </v-tabs>

        <!-- Login button -->
        <v-spacer></v-spacer>
        <v-menu
          transition="slide-y-transition"
        >
          <template v-slot:activator="{ props }">
            <v-btn
              v-bind="props"
              :style="{ marginRight: 30 + 'px', backgroundColor: '#28359', color: 'white' }"
            >
              Login
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(item, i) in buttonItems"
              :key="i"
              @click="handleItemClick(item)"
            >
              <v-list-item-title>{{item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </template>
    </v-toolbar>

    <v-window v-model="tab">
      <v-window-item
        v-for="(item,index) in items"
        :key="index"
        :value="index"
      >
        <v-card flat>
          <v-card-text v-text="item.text"></v-card-text>
        </v-card>
      </v-window-item>
    </v-window>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
        tab: null,
        items: [
          { label: 'Learning Journeys', text: 'Please Log In to view any Learning Journeys.' },
          { label: 'Skills', text: 'Please Log In to view Skills.' },
          { label: 'Courses', text: 'Please Log In to view Courses.' },
          { label: 'Jobs', text: 'Please Log In to view Jobs.' },
        ],
        buttonItems: [
          { title: 'Staff' },
          { title: 'HR' },
          { title: 'Manager' },
          ],
        };
      },
      methods: {
        handleItemClick(item){
          console.log('Clicked item: ${item.title}');
        },
      },
    };
</script>