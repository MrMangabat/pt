<template>
  <v-container class="py-6">
    <h1 class="text-h4 mb-4">Register</h1>
    <v-form @submit.prevent="submit">
      <v-row>
        <v-col cols="6">
          <v-text-field v-model="form.firstName" label="First Name" required />
        </v-col>
        <v-col cols="6">
          <v-text-field v-model="form.lastName" label="Last Name" required />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
          <v-text-field v-model="form.username" label="Username" required />
        </v-col>
        <v-col cols="6">
          <v-text-field v-model="form.email" label="Email" type="email" required />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="4">
          <v-text-field
            v-model.number="form.birthDay"
            label="Birth Day"
            type="number"
            min="1"
            max="31"
            required
          />
        </v-col>
        <v-col cols="4">
          <v-text-field
            v-model.number="form.birthMonth"
            label="Birth Month"
            type="number"
            min="1"
            max="12"
            required
          />
        </v-col>
        <v-col cols="4">
          <v-text-field
            v-model.number="form.birthYear"
            label="Birth Year"
            type="number"
            min="1900"
            required
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
          <v-select
            v-model="form.countryCode"
            :items="countryCodes"
            label="Country Code"
            required
          />
          <v-text-field
            v-model="form.phoneNumber"
            label="Phone Number"
            type="tel"
            inputmode="numeric"
            pattern="\\d*"
            required
          />
        </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="form.password"
            label="Password"
            type="password"
            required
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
          <v-text-field
            v-model="form.creationDate"
            label="Creation Date"
            type="date"
            readonly
          />
        </v-col>
      </v-row>
      <v-btn color="primary" large type="submit" class="mt-4">
        Submit
      </v-btn>
    </v-form>
  </v-container>
</template>

<script setup lang="ts">
import { reactive } from 'vue'

interface RegisterForm {
  firstName: string
  lastName: string
  birthDay: number | null
  birthMonth: number | null
  birthYear: number | null
  username: string
  email: string
  countryCode: string
  phoneNumber: string
  password: string
  creationDate: string
}

const countryCodes = ['+1', '+44', '+91', '+61', '+49', '+33', '+234', '+7']

const form = reactive<RegisterForm>({
  firstName: '',
  lastName: '',
  birthDay: null,
  birthMonth: null,
  birthYear: null,
  username: '',
  email: '',
  countryCode: countryCodes[0],
  phoneNumber: '',
  password: '',
  creationDate: new Date().toISOString().substr(0, 10)
})

function submit() {
  console.log('Registering user:', { ...form })
  // TODO: send form data to API
}
</script>
