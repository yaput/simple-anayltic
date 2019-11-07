function() {
        for (var evIdx in this.events) {
            if(this.events[evIdx].hasOwnProperty("parse_data")){
                if(this.events[evIdx].parse_data.intent.name == "default_fallback"){
                emit(this.events[evIdx].parse_data.text , 1);
                }
            }
        }
    }