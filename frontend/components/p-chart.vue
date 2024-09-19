<template>
  <v-card variant="flat"
    ><v-card-text>
      <v-chart
        class="chart"
        :option="finalOption"
        autoresize
        :style="{height: `${height}px`}"/></v-card-text
  ></v-card>
</template>

<script setup>
import VChart from "vue-echarts";
import * as echarts from 'echarts'; 
import { LineChart } from "echarts/charts";
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DataZoomComponent,
  ToolboxComponent,
} from "echarts/components";
use([
  CanvasRenderer,
  LineChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DataZoomComponent,
  ToolboxComponent,
]);
const props = defineProps({
  options: { required: false, default: [] },
  height: { required: false, default: '300' },
});
const baseOption = ref({
  backgroundColor:'transparent'
});
const finalOption = computed(() => {
  return { ...props.options, ...baseOption.value };
});
</script>
