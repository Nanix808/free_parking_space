<script>

import { ref, watch } from 'vue'

export default {

  props: {
    startvalue: {
      type: Number,
      default: 10
    },
  },

  emits: {
    percent: null,
  },

  setup(props, { emit }) {

    const value = ref(props.startvalue)

    watch(value, (count) => {
      emit("percent", count)
    })

    return {
      value,
    }
  }
}
</script>

<template>
  <div class="slider">
    <VueSlider :adsorb=true v-model="value" :tooltip-placement="['bottom']" :lazy="true" :use-keyboard="false">
    </VueSlider>
  </div>
</template>

<style lang="scss">
.slider {
  width: 100%;
}



/* rail style */
.vue-slider-rail {

  height: 0.7rem;
  box-shadow: inset 0.2rem 0.2rem 0.5rem var(--greyLight-2), inset -0.2rem -0.2rem 0.5rem var(--white);
  border-radius: 1rem;
}

/* process style */
.vue-slider-process {
  background: linear-gradient(-1deg, var(--primary-dark) 0%, var(--primary) 50%, var(--primary-light) 100%);
  border-radius: inherit;

}

/* mark style */
.vue-slider-mark {
  z-index: 4;

  @at-root &-step {
    width: 100%;
    height: 100%;


    &-active {}
  }

  @at-root &-label {

    white-space: nowrap;

    &-active {}
  }
}

/* dot style */
.vue-slider-dot {
  @at-root &-handle {
    cursor: pointer;
    position: relative;
    width: 0.8rem;
    height: 0.8rem;
    border-radius: 50%;
    box-shadow: inset 0.2rem 0.2rem 0.5rem var(--greyLight-2), inset -0.2rem -0.2rem 0.5rem var(--white);

    &::after {
      content: '';
      position: absolute;
      left: 50%;
      top: 50%;

      transform: translate(-50%, -50%) scale(1);
      z-index: -1;
      transition: transform 0.2s;
      width: 1.3rem;
      height: 1.3rem;
      border-radius: 50%;
      background: var(--white);
      box-shadow: 0px 0.1rem 0.3rem 0px var(--greyLight-3);
    }
  }

  @at-root &-tooltip {
    visibility: visible;
    border-radius: 0.6rem;


    @at-root &-show {
      .vue-slider-dot-tooltip-inner {
        opacity: 1;
        border-radius: 0.6rem;
        background: var(--greyLight-1);
      }
    }

    @at-root &-inner {

      opacity: 0;
      border-radius: 0.6rem;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary);
      height: 2.5rem;
      width: 3rem;
      box-shadow: 0.3rem 0.3rem 0.6rem var(--greyLight-2), -0.2rem -0.2rem 0.5rem var(--white);

      @at-root .vue-slider-dot-tooltip-text {

        white-space: nowrap;
        text-align: center;
        font-size: 1.2rem;
        color: var(--primary);

        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: content-box;
      }
    }
  }
}
</style>