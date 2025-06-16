<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>PT App</v-toolbar-title>
      <v-spacer />
      <v-btn text nuxt to="/landingpage">Home</v-btn>
      <v-btn text nuxt to="/screening">Screening</v-btn>
      <v-btn text nuxt to="/training-progression">Training Progression</v-btn>
      <v-btn text nuxt to="/contact">Contact</v-btn>
      <v-btn text nuxt to="/profile">Profile</v-btn>
      <v-btn text nuxt to="/exercise-library">Exercise Library</v-btn>
    </v-app-bar>
    <v-main>
      <slot />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
// Default layout with toolbar across all pages
</script>
