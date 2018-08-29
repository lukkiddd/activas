<template>
    <div class="mlr-auto at-row row container">
        <div class="col-md-24">
            <h1>Activas</h1>
        </div>
        <div class="col-md-24">
            <!-- label -->
            {{data.name}}

            <div class="row">
                <div
                    v-for="label in data.labels" 
                    :key="label"
                    :class="'col-md-' + (24/data.labels.length)">
                    <at-card class="label">
                        <div>
                            {{label}}
                        </div>
                        <div>
                            <small>(1)</small>
                        </div>
                    </at-card>  
                </div>
            </div>
        </div>
        <br>
        <br>
        <div class="col-md-24">
            <!-- labeled -->
            <h3>Labeled Data</h3>
            <at-table :columns="labeledColumns" :data="data.data.labeled"></at-table>

        </div>
    </div>
</template>

<script>
import ActivasServices from '@/services/ActivasService.js'
export default {
    mounted() {
        this.get()
    },
    data() {
        return {
            "data": () => {},
            "labeledColumns": [{
                "title": "text",
                "key": "text"
            }, {
                "title": "labels",
                "key": "labels",
                render: (h, params) => {
                    console.log(params)
                    return h('div', [
                        h('AtTag', {
                        props: {},
                        style: {}
                        }, params.item.labels[0])
                    ])
                }
            }]
        }
    },
    methods: {
        async get() {
            const response = await ActivasServices.get()
            this.data = response.data
        }
    }
}
</script>

<style scoped>
    .mlr-auto {
        margin-left: auto;
        margin-right: auto;
    }
    .label {
        text-align: center;
    }
</style>

