<script >
import { ref, computed, watchEffect, onMounted} from 'vue'
import ShowCam from '@/components/ShowCam.vue'
import UiButton from '@/components/ui/UiButton.vue'
import { useRouter } from 'vue-router'
import PopupPaint from '@/components/PopupPaint.vue';

export default {
  components: {
    ShowCam,
    UiButton,
    PopupPaint,
  },

  setup() {
    const router = useRouter()
    const rtsp = ref(null)
    const PopupOpen = ref(false)
    const name = ref(null)
    const start = ref(false)
    const test = ref(null)
    const canvas1 = ref(null)
    const canvasWidth = ref(300)
    const canvasHeight = ref(150)
    const backgroundImage = ref(null)
    const client_id = ref(100)
    const websoket = ref(false)
    const free = ref(false)
    const conf = ref(0.3)
    const iou = ref(0.7)


    const sendmesage = () => {
      websoket.value.send(JSON.stringify({
            conf: conf.value,
            iou: iou.value,
          }))
    }

    const change_conf = (value) => {
     conf.value = parseFloat(value) /100
     sendmesage()
    }
    const change_iou = (value) => {
      iou.value = parseFloat(value) /100
      sendmesage()
    }

    const button_click = () => {
      start.value = !start.value
    }
    const test_ok = () => {
      test.value = true
    }
    const test_false = () => {
      test.value = false
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

    const saveBD = (circle) => {
      fetch( `${process.env.VUE_APP_BASE_URL}parking/add`, {
        body: JSON.stringify({
          rtsp: rtsp.value,
          name: name.value,
          circle: circle,
          conf: conf.value,
          iou: iou.value
        }),
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'POST'
      }).then(function (response) {
        return response.json();
      }).then(function (answer) {
        start.value = false
        router.push({ name: 'first' })
        return answer;
      }).catch(function (e) {
        alert(e);
      });

    }

    const paint_click = async () => {
      let video = document.getElementById('video');
      canvasWidth.value = video.videoWidth
      canvasHeight.value = video.videoHeight
      PopupOpen.value = true
    }

    onMounted(() => {
      get_websoket_id()
    })

    watchEffect(() => rtsp.value ? test.value = null : '');
    return {
      activeButton: computed(() => rtsp.value && name.value ? true : false),

      test_ok,
      test_false,
      test,
      rtsp,
      name,
      button_click,
      paint_click,
      start,
      canvasWidth,
      canvasHeight,
      backgroundImage,
      canvas1,
      PopupOpen,
      saveBD,
      client_id,
      change_conf,
      change_iou
    };
  },
};
</script>

<template>
  <div class="settings_contents">
    <h1>Добавление видеокамеры в Базу данных</h1>
    <div class="input_container">
      <div class="form__group ">
        <input v-model="rtsp" type="input" class="form__field" placeholder="Введиде rtsp к камере" name="rtsp" id='rtsp'
          required />
      </div>
      <div class="form__group ">
        <input v-model="name" type="input" class="form__field" placeholder="Введиде название или адрес" name="name"
          id='name' required />
      </div>
    </div>
    <div class="cam_container">
      <UiButton :active=activeButton @clicks="button_click">Тест соединения</UiButton>
      <div class="cam_border">
        <div class="cam">
          <ShowCam :rtsp="rtsp" :start="start" :is_test="true" :settings="true" @test_ok="test_ok"
          :client_id="client_id"
            @test_false="test_false" />
        </div>
      </div>
    </div>
    <div class="paint_block">
      <UiButton :active=test @clicks="paint_click">Настройка свободных парковочных мест</UiButton>
    </div>
    <PopupPaint @saveBD="saveBD" @close="PopupOpen = false" 
    @conf="change_conf"
    @iou="change_iou" 
    :isOpen="PopupOpen" :canvasWidth="canvasWidth"
      :canvasHeight="canvasHeight" :backgroundImage="backgroundImage" />
  </div>
</template>

<style  lang="scss">
.settings_contents {
  width: 95%;
  margin: 0 auto;
  color: var(--primary);
  margin-top: 10px;
  height: 97vh;
  border-radius: 3rem;
  box-shadow: .8rem .8rem 1.4rem var(--greyLight-2),
    -.2rem -.2rem 1.8rem var(--white);
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;

  & .button {
    font-size: 1.3rem;
    height: 4rem;
  }
}
.input_container {

  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  width: 90%;
}
.form__group {
  width: 90%;
  position: relative;
  display: flex;
  align-items: center;
  margin: 10px 0;
  color: var(--greyDark);

  & input {
    width: 90%;
    height: 4rem;
    border: none;
    border-radius: 1rem;
    font-size: 1.4rem;
    padding-left: 3.8rem;
    box-shadow: var(--inner-shadow);
    background: none;
    font-family: inherit;
    color: var(--greyDark);

    &::placeholder {
      color: var(--greyLight-3);
    }

    &:focus {
      outline: none;
      box-shadow: var(--shadow);
      color: var(--greyDark);

    }
  }

}
.cam_container {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
  margin: 10px 0;

  & .cam_border {

    border: none;
    border-radius: 1rem;
    box-shadow: var(--inner-shadow);
    margin: 10px 0;
    padding: 10px;
    width: 90%;
    height: 38vh;

    display: flex;
    align-items: center;
    justify-content: center;

    & .cam {
      width: 100%;
      height: 100%;
    }
  }
}
</style>
