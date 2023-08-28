<template>
  <video id="video" autoplay="true" playsinline="true"></video>
</template>

<script>
import { toRef, watchEffect, onUnmounted } from 'vue'
export default {
  name: 'ShowCam',
  props: {
    start: Boolean,
    rtsp: String,
    client_id: {
      type: Number,
      default: 100
    },
    settings:{
      type: Boolean,
      default: false
    },
    is_test: {
      type: Boolean,
      default: false
    }

  },

  emits: {
    test_ok: null,
    test_false: null,

  },
  setup(props, { emit }) {

    const rtsp_show = toRef(() => props.rtsp)
    const start_video = toRef(() => props.start)
    const client_id = toRef(() => props.client_id)
    const test = toRef(() => props.is_test)
    const setting = toRef(() => props.settings)

    let pc = null;

    const negotiate = () => {
      pc.addTransceiver('video', { direction: 'recvonly' });
      pc.addTransceiver('audio', { direction: 'recvonly' });
      return pc.createOffer().then(function (offer) {
        return pc.setLocalDescription(offer);
      }).then(function () {
        // wait for ICE gathering to complete
        return new Promise(function (resolve) {
          if (pc.iceGatheringState === 'complete') {
            resolve();
          } else {
            /* eslint-disable */
            function checkState() {
              if (pc.iceGatheringState === 'complete') {
                pc.removeEventListener('icegatheringstatechange', checkState);
                resolve();
              }
            }
            pc.addEventListener('icegatheringstatechange', checkState);
          }
        });
      }).then(function () {
        var offer = pc.localDescription;
        return fetch(`${process.env.VUE_APP_BASE_URL}api/offer`, {
          body: JSON.stringify({
            sdp: offer.sdp,
            type: offer.type,
            client_id: client_id.value,
            setting: setting.value,
            rtsp: rtsp_show.value
          }),
          headers: {
            'Content-Type': 'application/json'
          },
          method: 'POST'
        });
      }).then(function (response) {
        return response.json();
      }).then(function (answer) {
        emit("test_ok")
        return pc.setRemoteDescription(answer);
      }).catch(function (e) {
        emit("test_false")
        // close()
        alert(e);
      });


    }
    const star_show_cam = () => {

      var config = {
        sdpSemantics: 'unified-plan'
      };
      pc = new RTCPeerConnection(config);

      // connect audio / video
      pc.addEventListener('track', function (evt) {
        if (evt.track.kind == 'video') {
          document.getElementById('video').srcObject = evt.streams[0];
          if (test.value){ document.getElementById('video1').srcObject = evt.streams[0]; }
        } else {
          document.getElementById('audio').srcObject = evt.streams[0];
        }
      });
      negotiate();
    };

    const stop = () => {
      // close peer connection
      if (pc) {
        pc.close();
        pc = null;
        console.log("Соединение закрыто")
      }

    }
    onUnmounted(() => {
      if (pc) {
        pc.close();
        pc = null;
      }
    })

    watchEffect(() => start_video.value ? star_show_cam() : stop());
    return {
      start_video,
      rtsp_show,
      star_show_cam,
    };
  }

}
</script>

<style scoped>
video {
  width: 100%;
  height: 100%;
}
</style>
