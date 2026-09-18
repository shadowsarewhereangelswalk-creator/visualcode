const wsUrl = document.getElementById("ws-url");
const wsMessage = document.getElementById("ws-message");
const wsStatus = document.getElementById("ws-status");
let socket = null;

document.getElementById("ws-connect").addEventListener("click", () => {
  if (socket && socket.readyState <= WebSocket.OPEN) {
    socket.close();
  }

  try {
    socket = new WebSocket(wsUrl.value.trim());
    wsStatus.textContent = "Conectando…";
    socket.addEventListener("open", () => { wsStatus.textContent = "Conectado."; });
    socket.addEventListener("message", (event) => {
      wsStatus.textContent = "Mensaje recibido:\n" + String(event.data);
    });
    socket.addEventListener("close", () => { wsStatus.textContent = "Conexión cerrada."; });
    socket.addEventListener("error", () => {
      wsStatus.textContent = "Error de WebSocket. Verifica la URL o utiliza tu propio servidor.";
    });
  } catch (error) {
    wsStatus.textContent = "No se pudo crear la conexión: " + error.message;
  }
});

document.getElementById("ws-send").addEventListener("click", () => {
  if (!socket || socket.readyState !== WebSocket.OPEN) {
    wsStatus.textContent = "Primero debes abrir una conexión WebSocket.";
    return;
  }
  socket.send(wsMessage.value);
  wsStatus.textContent = "Mensaje enviado: " + wsMessage.value;
});

document.getElementById("ws-close").addEventListener("click", () => {
  if (socket) socket.close();
});

const localVideo = document.getElementById("local-video");
const remoteVideo = document.getElementById("remote-video");
const rtcStatus = document.getElementById("rtc-status");
let localStream = null;
let senderPeer = null;
let receiverPeer = null;

async function startCamera() {
  if (localStream) return localStream;
  localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
  localVideo.srcObject = localStream;
  rtcStatus.textContent = "Cámara activa.";
  return localStream;
}

document.getElementById("camera-start").addEventListener("click", async () => {
  try {
    await startCamera();
  } catch (error) {
    rtcStatus.textContent = "No se pudo activar la cámara: " + error.message;
  }
});

document.getElementById("rtc-connect").addEventListener("click", async () => {
  try {
    await startCamera();

    if (senderPeer) senderPeer.close();
    if (receiverPeer) receiverPeer.close();

    senderPeer = new RTCPeerConnection();
    receiverPeer = new RTCPeerConnection();

    senderPeer.addEventListener("icecandidate", async (event) => {
      if (event.candidate) await receiverPeer.addIceCandidate(event.candidate);
    });
    receiverPeer.addEventListener("icecandidate", async (event) => {
      if (event.candidate) await senderPeer.addIceCandidate(event.candidate);
    });
    receiverPeer.addEventListener("track", (event) => {
      remoteVideo.srcObject = event.streams[0];
    });

    localStream.getTracks().forEach((track) => senderPeer.addTrack(track, localStream));

    const offer = await senderPeer.createOffer();
    await senderPeer.setLocalDescription(offer);
    await receiverPeer.setRemoteDescription(offer);

    const answer = await receiverPeer.createAnswer();
    await receiverPeer.setLocalDescription(answer);
    await senderPeer.setRemoteDescription(answer);

    rtcStatus.textContent = "Conexión WebRTC local establecida.";
  } catch (error) {
    rtcStatus.textContent = "Error WebRTC: " + error.message;
  }
});

document.getElementById("rtc-stop").addEventListener("click", () => {
  if (senderPeer) senderPeer.close();
  if (receiverPeer) receiverPeer.close();
  senderPeer = null;
  receiverPeer = null;

  if (localStream) {
    localStream.getTracks().forEach((track) => track.stop());
    localStream = null;
  }

  localVideo.srcObject = null;
  remoteVideo.srcObject = null;
  rtcStatus.textContent = "WebRTC detenido.";
});
