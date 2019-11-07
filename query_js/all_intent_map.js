 function() {
        for (var evIdx in this.events) {
            if(this.events[evIdx].event == "user"){
                if(this.events[evIdx].hasOwnProperty("parse_data")){
                    emit(this.events[evIdx].parse_data.intent , 1);

                }
        }
    }
}