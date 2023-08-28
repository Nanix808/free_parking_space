<script>
import { toRef } from 'vue'

export default {
  props: {
    active: {
      type: Boolean,
      required: false,
    },
  },

  emits: ['clicks'],

  setup(props, { emit }) {

    const activebutton = toRef(() => props.active)
    const click = () => {
      activebutton.value ? emit("clicks") : ''
    }

    return {
      activebutton,
      click,

    };
  }
}
</script>

<template>
  <button class="button" :class="activebutton ? 'active_button' : ''" @click="click"><p>
        <slot></slot>
  </p></button>
</template>
<style lang="scss" >

.button {
  border: 0;
  border-radius: 1rem;
  box-shadow: var(--shadow);
  justify-self: center;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: .3s ease;
  background: var(--greyLight-1);
  color: var(--greyDark);

  &:hover { color: var(--primary); }
  &:active {
      box-shadow: var(--inner-shadow);
    }

  & p {
    display: flex;
    justify-content: space-between;
    align-items: center;

    & svg{
      padding-right: 5px;
    }
  }  
}

</style>