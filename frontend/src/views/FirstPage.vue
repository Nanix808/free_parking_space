<script >
import { ref, onMounted, onUnmounted } from 'vue';
import ShowCam from '@/components/ShowCam.vue'
import { useRouter } from 'vue-router'

export default {

  components: {
    ShowCam,
  },

  setup() {

    const router = useRouter()
    const parking = ref([])
    const rtsp = ref(null)
    const startcam = ref(false)
    const free = ref(false)
    const client_id = ref(0)
    const websoket = ref(false)

    const settings = () => {
      startcam.value = false
      free.value = 0
      router.push({ name: 'settings' })
    }
    const selectParking = (item) => {
      if (websoket.value) {
        websoket.value.close()
      }
      get_websoket_id()
      startcam.value = false
      free.value = false
      rtsp.value = item.rtsp
      setTimeout(function () {
        startcam.value = true

      }, 500);

    }
    const get_client_id = () => {
      return client_id.value = Date.now()
    }
    const get_websoket_id = () => {
      client_id.value = get_client_id()
      websoket.value = new WebSocket(`${process.env.VUE_APP_BASE_WEBSOKET_URL}${client_id.value}`);
      websoket.value.onmessage = (event) => {
        free.value = JSON.parse(event.data)
      }
    }
    const get_all_parking = () => {
     
      fetch(`${process.env.VUE_APP_BASE_URL}parking/show`, {

        headers: {
          'Content-Type': 'application/json'
        },
        method: 'GET',
        

      }).then(function (response) {
        return response.json();
      }).then(function (answer) {
        parking.value = answer
      }).catch(function (e) {
        alert(e);
      });
    }
    onMounted(() => {
      get_all_parking()
    })

    onUnmounted(() => {
      startcam.value = false
    })

    return {
      settings,
      parking,
      selectParking,
      rtsp,
      startcam,
      free,
      get_all_parking,
      client_id,
    };
  },
};
</script>

<template>
  <div class="page_content">
    <div class="information">
      <p>Свободно:</p>
      <div class="circle">
        <span :class="free.free ? '' : 'shadow'" class="circle__btn">
        {{ free.free }}
       
        </span>
        <span :class="free.free ? '' : 'paused'" class="circle__back-1"></span>
        <span :class="free.free ? '' : 'paused'" class="circle__back-2"></span>
      </div>
      <p>из:</p>
      <div class="circle">
        <span :class="free.free ? '' : 'shadow'" class="circle__btn">
          {{ free.all }}
        </span>
        <span :class="free.free ? '' : 'paused'" class="circle__back-1"></span>
        <span :class="free.free ? '' : 'paused'" class="circle__back-2"></span>
      </div>
    </div>
    <div class="all_parking_content">
      <div class="button_block">
        <button class="parking_item btn btn__primary" @click="selectParking(item)" v-for="(item, index) in parking"
          :key="index">
          <p>{{ item.name }}</p>
        </button>
      </div>
      <div class="live_cam">
        <div class="cam_content">
          <ShowCam :rtsp="rtsp" :start="startcam" :client_id="client_id" />
        </div>
      </div>
    </div>
    <div class="settings_content">
      <button class="btn btn__primary" @click="settings">
        <p>Настройки </p>
      </button>
    </div>
  </div>
</template>


<style lang="scss">
.all_parking_content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
  width: 100%;
}

.page_content {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
}

.information {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 90%;
  padding: 13px 1rem;
  border-radius: 3rem;
  box-shadow: .8rem .8rem 1.4rem var(--greyLight-2),
    -.2rem -.2rem 1.8rem var(--white);
}

.information p {
  margin: 0px 20px;
  font-size: 2.2rem;
  color: var(--primary);
}

.button_block {
  display: flex;
  align-items: center;
  justify-content: space-around;
  width: 90%;
  padding: 0 1rem;
  min-height: 3rem;
}

.btn {
  height: 2.5rem;
  width: 100%;
  border-radius: 1rem;
  box-shadow: var(--shadow);
  justify-self: center;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: .3s ease;
  margin: 8px;
  flex: 1 0 0px;

  &__primary {
    background: var(--primary);
    box-shadow: inset .2rem .2rem 1rem var(--primary-light),
      inset -.2rem -.2rem 1rem var(--primary-dark),
      var(--shadow);
    ;
    color: var(--greyLight-1);

    &:hover {
      color: var(--white);
    }

    &:active {
      box-shadow: inset .2rem .2rem 1rem var(--primary-dark),
        inset -.2rem -.2rem 1rem var(--primary-light);
    }
  }

  p {
    font-size: 1.6rem;
  }
}

.live_cam {

  border-radius: 3rem;
  box-shadow: .8rem .8rem 1.4rem var(--greyLight-2),
    -.2rem -.2rem 1.8rem var(--white);
  padding: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 90%;
  height: 69vh;
}

.cam_content {
  width: 100%;
  height: 100%;
}

.settings_content {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 10px;
}


/*  PLAY BUTTON  */
.circle {

  justify-self: center;
  border-radius: 1rem;
  display: grid;
  grid-template-rows: 1fr;
  justify-items: center;
  align-items: center;

  &__btn {
    grid-row: 1 / 2;
    grid-column: 1 / 2;
    width: 4rem;
    height: 4rem;
    display: flex;
    margin: .6rem;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    font-size: 3.2rem;
    color: var(--primary);
    z-index: 300;
    background: var(--greyLight-1);
    box-shadow: var(--shadow);
    cursor: pointer;
    position: relative;

    &.shadow {
      box-shadow: var(--inner-shadow);
    }

    .play {
      position: absolute;
      opacity: 0;
      transition: all .2s linear;

      &.visibility {
        opacity: 1;
      }
    }

    .pause {
      position: absolute;
      transition: all .2s linear;

      &.visibility {
        opacity: 0;
      }
    }
  }

  &__back-1,
  &__back-2 {
    grid-row: 1 / 2;
    grid-column: 1 / 2;
    width: 3.5rem;
    height: 3.5rem;
    border-radius: 50%;
    filter: blur(1px);
    z-index: 100;
  }

  &__back-1 {
    box-shadow: .4rem .4rem .8rem var(--greyLight-2),
      -.4rem -.4rem .8rem var(--white);
    background: linear-gradient(to bottom right, var(--greyLight-2) 0%, var(--white) 100%);
    animation: waves 4s linear infinite;

    &.paused {
      animation-play-state: paused;
    }
  }

  &__back-2 {
    box-shadow: .4rem .4rem .8rem var(--greyLight-2),
      -.4rem -.4rem .8rem var(--white);
    animation: waves 4s linear 2s infinite;

    &.paused {
      animation-play-state: paused;
    }
  }
}


@keyframes waves {
  0% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    opacity: 1;
  }

  100% {
    transform: scale(2);
    opacity: 0;
  }
}
</style>