"""
Auto generated file, DO NOT EDIT!
"""



class HTTPValidationError{
    HTTPValidationError(, {List detail=null, }){
        this.detail = detail;
        
    }

    Map<string, dynamic> toDict(){
        Map<string, dynamic> dict;
        dict["detail"] = this.detail;
        
        return dict;
    }

    HTTPValidationError.fromDict(Map<string, dynamic> dict){
        this.detail = dict["detail"]
        
    }
}

class ValidationError{
    ValidationError(, Listloc, Stringmsg, Stringtype, {}){
        this.loc = loc;
        this.msg = msg;
        this.type = type;
        
    }

    Map<string, dynamic> toDict(){
        Map<string, dynamic> dict;
        dict["loc"] = this.loc;
        dict["msg"] = this.msg;
        dict["type"] = this.type;
        
        return dict;
    }

    ValidationError.fromDict(Map<string, dynamic> dict){
        this.loc = dict["loc"]
        this.msg = dict["msg"]
        this.type = dict["type"]
        
    }
}
