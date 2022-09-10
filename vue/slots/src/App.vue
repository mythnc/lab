<template>
  <app-form>
    <template #helper>{{ msg }}</template>
    <template #fields>
      <input type="text" placeholder="email" />
    </template>
    <template #buttons>
      <button type="submit">Submit</button>
    </template>
  </app-form>
  <app-form>
    <template #helper>Form 2</template>
    <template #fields>
      <input type="text" placeholder="username" />
    </template>
    <template #buttons>
      <button type="cancel">Cancel</button>
    </template>
  </app-form>
</template>

<script>
import AppForm from "@/components/Form.vue";

export default {
  name: "App",
  components: {
    AppForm,
  },
  data() {
    return {
      msg: "Form 1",
    };
  },
};
</script>
