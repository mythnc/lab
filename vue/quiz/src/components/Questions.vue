<template>
  <div class="questions-ctr">
    <div class="progress">
      <div class="bar" :style="bar"></div>
      <div class="status">{{ status }}</div>
    </div>
    <TransitionGroup name="fade">
      <div
        class="single-question"
        v-for="(question, questionIndex) in questions"
        :key="question.q"
        v-show="questionIndex == questionsAnswered"
      >
        <div class="question">{{ question.q }}</div>
        <div class="answers">
          <div
            class="answer"
            v-for="answer in question.answers"
            :key="answer.text"
            @click.prevent="selectAnswer(answer.is_correct)"
          >
            {{ answer.text }}
          </div>
        </div>
      </div>
    </TransitionGroup>
  </div>
</template>

<script>
export default {
  name: "QuizQuestions",
  props: ["questions", "questionsAnswered"],
  emits: ["questionAnswered"],
  computed: {
    status() {
      return `${this.questionsAnswered} out of ${this.questions.length} questions answered`;
    },
    bar() {
      return {
        width: `${(this.questionsAnswered / this.questions.length) * 100}%`,
      };
    },
  },
  methods: {
    selectAnswer(is_correct) {
      this.$emit("question-answered", is_correct);
    },
  },
};
</script>
