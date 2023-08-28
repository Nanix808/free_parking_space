<template>
  <div v-show="Open" class="backdrop" @mousedown="close">
    <div class="popup" @mousedown.stop>
      <div class="popup_container">
        <div class="popup_header">
          <h3>Нарисуйте парковочные места</h3>
          <div class="button-container">
            <UiButton :active=true @click.prevent="video_image_change">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-play"
                viewBox="0 0 16 16">
                <path
                  d="M10.804 8 5 4.633v6.734L10.804 8zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696l6.363 3.692z" />
              </svg>
              Пуск / Стоп
            </UiButton>
            <UiButton :active=true @click.prevent="undo">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                class="bi bi-arrow-counterclockwise" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 3a5 5 0 1 1-4.546 2.914.5.5 0 0 0-.908-.417A6 6 0 1 0 8 2v1z" />
                <path
                  d="M8 4.466V.534a.25.25 0 0 0-.41-.192L5.23 2.308a.25.25 0 0 0 0 .384l2.36 1.966A.25.25 0 0 0 8 4.466z" />
              </svg>
              Отменить
            </UiButton>
            <UiButton :active=true @click.prevent="reset">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                class="bi bi-file-earmark" viewBox="0 0 16 16">
                <path
                  d="M14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L14 4.5zm-3 0A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V4.5h-2z" />
              </svg>
              Сбросить
            </UiButton>
            <UiButton :active=true @click.prevent="save">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-image-alt"
                viewBox="0 0 16 16">
                <path
                  d="M7 2.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0zm4.225 4.053a.5.5 0 0 0-.577.093l-3.71 4.71-2.66-2.772a.5.5 0 0 0-.63.062L.002 13v2a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-4.5l-4.777-3.947z" />
              </svg>
              Сохранить в БД
            </UiButton>
          </div>
          <div class="popup_close" @click="close">
            <div></div>
          </div>
        </div>
        <div class="coef_container">
          <div class="coef">
            <p>Порог</p>
            <UiSlider @percent="change_conf" :startvalue=25 />
          </div>
          <div class="iou">
            <p>IoU</p>
            <UiSlider @percent="change_iou" :startvalue=70 />
          </div>
        </div>
        <div class="content">
          <div class="canvas_content">
            <div class="canvas_paint" :width="Width" :height="Height">
              <canvas id="mycanvas_backround" ref="VueCanvasBackground" :width="Width" :height="Height"
                v-show="!play"></canvas>
              <video id="video1" autoplay="true" playsinline="true" :width="Width" :height="Height" v-show="play"></video>
              <canvas id="mycanvas" ref="VueCanvasDrawing" :width="Width" :height="Height" @mousedown="canvasMouseDown"
                @mousemove="canvasMouseMove" @mouseup="canvasMouseUp">
              </canvas>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, toRef, onMounted, onUnmounted } from 'vue'
import UiButton from '@/components/ui/UiButton.vue';
import UiSlider from '@/components/ui/UiSlider.vue';

export default {

  components: {
    UiButton,
    UiSlider,
  },

  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },

    canvasWidth: Number,
    canvasHeight: Number,
    backgroundImage: String,
  },

  emits: {
    close: null,
    ok: null,
    saveBD: null,
    conf: null,
    iou: null
  },

  setup(props, { emit }) {
    const Open = toRef(() => props.isOpen)
    const Width = toRef(() => props.canvasWidth)
    const Height = toRef(() => props.canvasHeight)
    const ctx = ref(null)
    const ctxBackround = ref(null)
    const VueCanvasDrawing = ref()
    const VueCanvasBackground = ref()
    const circles = ref([])
    const play = ref(true)


    let markerColor = "#FF0000";
    let mouseX = 0;
    let mouseY = 0;
    let startX = 0, startY = 0;
    let radius = 0;
    let isMouseDown = false;

    const change_conf = (value) => {
      emit("conf", value)
    }

    const change_iou = (value) => {
      emit("iou", value)
    }

    const getDistance = (p1X, p1Y, p2X, p2Y) => {
      return Math.sqrt(Math.pow(p1X - p2X, 2) + Math.pow(p1Y - p2Y, 2))
    }

    const video_image_change = () => {

      play.value = !play.value

      let canvas = document.getElementById('mycanvas_backround');
      let video = document.getElementById('video1');
      let ctx = canvas.getContext('2d');
      ctx.drawImage(video, 0, 0, Width.value, Height.value);

    }

    const drawCircle = (circle) => {
      let { x1, y1, rad } = circle
      ctx.value.beginPath();
      ctx.value.arc(x1, y1, rad, 0, 2 * Math.PI);
      ctx.value.strokeStyle = markerColor;
      ctx.value.stroke();
    }

    const canvasMouseDown = (event) => {
      startX = event.offsetX;
      startY = event.offsetY;
      isMouseDown = true;
    }

    const canvasMouseUp = () => {
      isMouseDown = false;
      if (radius > 2) {
        circles.value.push({
          x1: startX,
          y1: startY,
          rad: radius,
          x2: mouseX,
          y2: mouseY
        })
      }
      radius = 0
    }

    const canvasMouseMove = (event) => {

      if (!isMouseDown) {
        return;
      }
      ctx.value.clearRect(0, 0, Width.value, Height.value);
      mouseX = parseInt(event.offsetX);
      mouseY = parseInt(event.offsetY);
      radius = getDistance(startX, startY, mouseX, mouseY);
      circles.value.forEach(function (circ) {
        drawCircle(circ)
      });
      drawCircle({ x1: startX, y1: startY, rad: radius })
    }


    const undo = () => {
      circles.value.pop()
      ctx.value.clearRect(0, 0, Width.value, Height.value);
      circles.value.forEach(function (circ) {
        drawCircle(circ)
      });
    }

    const reset = () => {
      circles.value = []
      ctx.value.clearRect(0, 0, Width.value, Height.value);

    }

    const save = () => {
      if (circles.value.length) {
        emit("saveBD", circles.value);
        emit("close");
      }
      else {
        alert('Не выбранны парковочные места')
      }
    }

    const close = () => {
      emit("close");
    };

    const handleKeydown = (e) => {
      if (Open.value && e.key === "Escape") {
        close();
      }
    }

    onMounted(() => {
      ctx.value = VueCanvasDrawing.value.getContext('2d')
      ctxBackround.value = VueCanvasBackground.value.getContext('2d')
      document.addEventListener("keydown", handleKeydown);
    })
    onUnmounted(() => {
      document.removeEventListener("keydown", handleKeydown)
    })

    return {
      Open,
      close,
      Width,
      Height,
      undo,
      reset,
      save,
      play,
      VueCanvasDrawing,
      VueCanvasBackground,
      canvasMouseDown,
      canvasMouseMove,
      canvasMouseUp,
      video_image_change,
      change_conf,
      change_iou,
    }
  },
}
</script>
<style lang="scss">
video1 {
  width: 40px;
  height: 50px;
}

.popup {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 95%;
  transform: translate(-50%, -50%);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, .1);
  display: flex;
  flex-direction: column;
  cursor: default;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;

  & button.button {
    font-size: 1rem;
    height: 40px;
    margin: 0 20px;
  }
}

.popup_container {
  position: relative;
  display: flex;
  flex-direction: column;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  background: var(--greyLight-1);
}

.popup_header {
  height: 60px;
  padding: 8px;
  background-color: rgb(245, 245, 245);
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgb(221, 221, 221);
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  background: var(--greyLight-1);
}

.popup h3 {
  padding: 5px;
}

.popup_close {
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;

}

.popup_close div {
  width: 20px;
  height: 20px;
  border-radius: 512px;
  background-size: cover;
  background: url(../assets/images/close.svg);
}

.popup_close:hover {
  background-color: var(--greyLight-2);
  border-radius: 512px;
}

.popup_close div:hover {
  background-size: cover;
  background: url(../assets/images/close-hover.svg);
}

.coef_container {
  width: 100%;
  height: 40px;
  // background-color: red;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.coef,
.iou {
  width: 250px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;

  & p {
    padding-right: 10px;
    padding-top: 4px;
  }
}


.content {
  background: var(--greyLight-1);
  display: flex;
  justify-content: center;
  align-items: center;
}

.canvas_content {

  border-radius: 3rem;
  box-shadow: .8rem .8rem 1.4rem var(--greyLight-2),
    -.2rem -.2rem 1.8rem var(--white);
  padding: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 90%;
  height: 75vh;
  margin: 15px 0;
}

.backdrop {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 100;
}

.canvas_paint {
  overflow-y: auto;
  overflow-x: auto;
  position: relative;
  width: 100%;
  height: 100%;
}

.canvas_paint::-webkit-scrollbar {
  background: var(--greyLight-1);
  width: 14px;
}

.canvas_paint::-webkit-scrollbar-thumb {
  border: 4px solid rgba(0, 0, 0, 0);
  background-clip: padding-box;
  border-radius: 9999px;
  background-color: var(--primary);
}

#mycanvas {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 2;
}

.button-container {
  display: flex;
  align-items: center;
  justify-content: space-around;
}
</style>
