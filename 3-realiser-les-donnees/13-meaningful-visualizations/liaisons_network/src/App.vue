<style src="vue-d3-network/dist/vue-d3-network.css"></style>
<template>
  <div id="app">
    <d3-network
      :net-nodes="nodes"
      :net-links="links"
      :options="options"
    ></d3-network>
  </div>
</template>

<script>
import D3Network from "vue-d3-network";

export default {
  components: {
    D3Network,
  },
  data() {
    return {
      nodes: [
        { id: 1, name: "192.168.2.1" },
        { id: 2, name: "192.168.2.128" },
        { id: 3, name: "192.168.2.2", _color: "orange" },
        { id: 4, name: "192.168.2.3" },
        { id: 5, name: "192.168.2.4" },
        { id: 6, name: "192.168.2.5" },
        { id: 7, name: "192.168.2.6" },
        { id: 8, name: "192.168.2.7" },
        { id: 9, name: "192.168.2.254" },
        { id: 10, name: "192.168.2.8" },
      ],
      links: [
        { sid: 1, tid: 2, _color: "red" },
        { sid: 2, tid: 8, _color: "f0f" },
        { sid: 3, tid: 4, _color: "rebeccapurple" },
        { sid: 4, tid: 5 },
        { sid: 5, tid: 6 },
        { sid: 7, tid: 8 },
        { sid: 5, tid: 8 },
        { sid: 3, tid: 8 },
        { sid: 7, tid: 9 },
        { sid: 9, tid: 10, _color: "blue" },
      ],
      options: {
        force: 3000,
        nodeSize: 15,
        nodeLabels: true,
        linkWidth: 5,
      },
    };
  },
};
</script>