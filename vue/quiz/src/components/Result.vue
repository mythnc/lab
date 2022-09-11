<template>
  <div class="result">
    <div class="title">{{ title }}</div>
    <div class="desc">{{ desc }}</div>
  </div>
</template>

<script>
export default {
  name: "Result",
  props: ["results", "totalCorrect"],
  computed: {
    title() {
      return this.results.find((result) => result.min <= this.totalCorrect && result.max >= this.totalCorrect).title;
    },
    desc() {
      return this.results.find((result) => result.min <= this.totalCorrect && result.max >= this.totalCorrect).desc;
    },
  },
};
</script>
