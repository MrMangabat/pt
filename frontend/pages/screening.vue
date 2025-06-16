<template>
  <div>
    <section class="p-6 max-w-2xl mx-auto">
      <h1 class="text-2xl font-bold mb-4">Submission Form</h1>
      <form @submit.prevent="onSubmit" class="space-y-6">
        <!-- Client Info -->
        <fieldset>
          <legend class="font-semibold">Client Info</legend>
          <div>
            <label>Name</label>
            <input v-model="form.name" type="text" required />
          </div>
          <div>
            <label>Date of Birth</label>
            <input v-model="form.date_of_birth" type="date" required />
          </div>
          <div>
            <label>Email</label>
            <input v-model="form.email" type="email" required />
          </div>
          <div>
            <label>Phone</label>
            <input v-model="form.phone" type="tel" required />
          </div>
          <div>
            <label>Age</label>
            <input v-model.number="form.age" type="number" min="0" required />
          </div>
          <div>
            <label>Weight (kg)</label>
            <input v-model.number="form.weight" type="number" step="0.1" min="0" required />
          </div>
          <div>
            <label>Height (cm)</label>
            <input v-model.number="form.height" type="number" step="0.1" min="0" required />
          </div>
        </fieldset>

        <!-- Health Status -->
        <fieldset>
          <legend class="font-semibold">Health Status</legend>
          <div>
            <label>Previous Injuries</label>
            <textarea v-model="form.previous_injuries" rows="2"></textarea>
          </div>
          <div>
            <label>Active Injuries</label>
            <textarea v-model="form.active_injuries" rows="2"></textarea>
          </div>
          <div>
            <label>Medications</label>
            <textarea v-model="form.medications" rows="2"></textarea>
          </div>
          <div>
            <label>Pain Points</label>
            <textarea v-model="form.pain_points" rows="2"></textarea>
          </div>
        </fieldset>

        <!-- Training History -->
        <fieldset>
          <legend class="font-semibold">Training History</legend>
          <div>
            <label>Prior Training Types (comma-separated)</label>
            <input v-model="form.prior_training_types" type="text" placeholder="e.g. yoga, weightlifting" />
          </div>
          <div>
            <label>Motivation Text</label>
            <textarea v-model="form.motivation_text" rows="3"></textarea>
          </div>
        </fieldset>

        <!-- Goals -->
        <fieldset>
          <legend class="font-semibold">Goals</legend>
          <v-combobox
            v-model="form.goals"
            :items="goalsOptions"
            label="Select up to two main goals"
            multiple
            chips
          />
        </fieldset>

        <!-- VO₂max -->
        <fieldset>
          <legend class="font-semibold">VO₂max Test</legend>
          <div>
            <label>Test Type</label>
            <input v-model="form.test_type" type="text" placeholder="e.g. running, rowing" />
          </div>
          <div>
            <label>Result (ml/kg/min)</label>
            <input v-model.number="form.result" type="number" step="0.1" />
          </div>
          <div>
            <label>VO₂max Group</label>
            <select v-model="form.vo2max_group">
              <option disabled value="">Select group</option>
              <option v-for="group in vo2maxGroups" :key="group" :value="group">{{ group }}</option>
            </select>
          </div>
        </fieldset>

        <!-- Reflection -->
        <fieldset>
          <legend class="font-semibold">Reflection</legend>
          <div>
            <label>Why Test</label>
            <textarea v-model="form.why_test" rows="2"></textarea>
          </div>
          <div>
            <label>Result Reaction</label>
            <textarea v-model="form.result_reaction" rows="2"></textarea>
          </div>
          <div>
            <label>Training Use Intent</label>
            <textarea v-model="form.training_use_intent" rows="2"></textarea>
          </div>
          <div>
            <label>Should Prioritize</label>
            <textarea v-model="form.should_prioritize" rows="2"></textarea>
          </div>
        </fieldset>

        <div>
          <v-btn type="submit" color="primary" variant="contained" dark>Submit</v-btn>
        </div>
      </form>
    </section>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue';
import { useFetch } from '#app';

const form = reactive({
  name: '',
  date_of_birth: '',
  email: '',
  phone: '',
  previous_injuries: '',
  active_injuries: '',
  medications: '',
  pain_points: '',
  prior_training_types: <string[]>[],
  motivation_text: '',
  goals: <string[]>[],
  test_type: '',
  result: 0,
  vo2max_group: '',
  why_test: '',
  result_reaction: '',
  training_use_intent: '',
  should_prioritize: '',
  age: 0,
  weight: 0,
  height: 0
});

const goalsOptions = ['strength', 'mobility', 'cardio', 'weightloss', 'functional'];
const vo2maxGroups = ['very low', 'low', 'average', 'good', 'very good', 'elite'];

async function onSubmit() {
  try {
    const { data, error } = await useFetch('http://localhost:8000/submit-form-data', {
      method: 'POST',
      body: form
    });
    if (error.value) {
      alert('Submission failed');
    } else {
      alert('Submission successful');
    }
  } catch (err) {
    alert('Submission failed');
  }
}
</script>

<style scoped>
label { display: block; margin-top: 0.5rem; font-weight: 500; }
input, textarea, select { width: 100%; padding: 0.5rem; margin-top: 0.25rem; border: 1px solid #ccc; border-radius: 4px; }
fieldset { border: 1px solid #ddd; padding: 1rem; border-radius: 4px; }
legend { padding: 0 0.5rem; }
button { cursor: pointer; }
</style>
