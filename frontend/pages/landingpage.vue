<template>
  <v-app>
    <!-- Toolbar -->
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>PT App</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <!-- Row 1: Hero Intro -->
        <v-row>
          <v-col cols="2" />
          <v-col cols="8">
            <v-card class="pa-4">
              <h2 class="text-h4 mb-2">Welcome to My Personal Training site</h2>
              <p>Personalized training plans to help you reach your fitness goals.</p>
              <p>Whether you're looking to lose weight, build muscle, or improve your overall fitness, I can help you get there.</p>
              <p></p>
            </v-card>
          </v-col>
          <v-col cols="2" />
        </v-row>

        <!-- Row 2: Who I Am -->
        <v-row>
          <v-col cols="2" />
          <v-col cols="8">
            <v-card class="pa-4">
              <h3 class="text-h5 mb-2">Who I Am</h3>
              <p>I'm a international certified personal trainer from Inspire Institute https://www.inspire-institute.dk/ by Henrik Duer</p>
              <p>I come with a background in Economics & IT supplemented with a master in Data Science.</p>
              <p>M goal is to implement and utilize AI/ML models to enhance out training experiences and output, simply put, lets utilize technology when we are training</p>
              <p>My approach is data-driven, focusing on measurable results and continuous improvement.</p>
            </v-card>
          </v-col>
          <v-col cols="2" />
        </v-row>

        <!-- Row 3: What I Can Offer -->
        <v-row>
          <v-col cols="2" />
          <v-col cols="8">
            <v-card class="pa-4">
              <h3 class="text-h5 mb-2">What I Can Offer</h3>
              <p>One-on-one exercise guidance, group sessions, and customized workout programs.</p>
            </v-card>
          </v-col>
          <v-col cols="2" />
        </v-row>

        <!-- Row 4: Get Started CTA -->
        <v-row>
          <v-col cols="2" />
          <v-col cols="8" class="text-center">
            <v-btn color="primary" to="/screening" large>Get Started</v-btn>
          </v-col>
          <v-col cols="2" />
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>