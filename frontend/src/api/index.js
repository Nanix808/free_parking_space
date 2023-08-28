import {DefaultApiInstance} from './apiinstanse.js'





export const UrlApi = {

    postResume(body) {
        const url = '/resume';
        // const body =  body
        return DefaultApiInstance.post(url,body)
    },

  




}
