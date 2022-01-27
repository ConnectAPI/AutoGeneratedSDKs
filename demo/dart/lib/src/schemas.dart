"""
Auto generated file, DO NOT EDIT!
"""



class BodyFileOptional{
    BodyFileOptional(, {String a=null, }){
        this.a = a;
        
    }

    Map<string, dynamic> toDict(){
        Map<string, dynamic> dict;
        dict["a"] = this.a;
        
        return dict;
    }

    BodyFileOptional.fromDict(Map<string, dynamic> dict){
        this.a = dict["a"]
        
    }
}

class BodyFile{
    BodyFile(, Stringa, {}){
        this.a = a;
        
    }

    Map<string, dynamic> toDict(){
        Map<string, dynamic> dict;
        dict["a"] = this.a;
        
        return dict;
    }

    BodyFile.fromDict(Map<string, dynamic> dict){
        this.a = dict["a"]
        
    }
}

class BodyFormOptional{
    BodyFormOptional(, {String a=null, }){
        this.a = a;
        
    }

    Map<string, dynamic> toDict(){
        Map<string, dynamic> dict;
        dict["a"] = this.a;
        
        return dict;
    }

    BodyFormOptional.fromDict(Map<string, dynamic> dict){
        this.a = dict["a"]
        
    }
}

class BodyForm{
    BodyForm(, Stringa, {}){
        this.a = a;
        
    }

    Map<string, dynamic> toDict(){
        Map<string, dynamic> dict;
        dict["a"] = this.a;
        
        return dict;
    }

    BodyForm.fromDict(Map<string, dynamic> dict){
        this.a = dict["a"]
        
    }
}

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

class Nested{
    Nested(, {int a=null, }){
        this.a = a;
        
    }

    Map<string, dynamic> toDict(){
        Map<string, dynamic> dict;
        dict["a"] = this.a;
        
        return dict;
    }

    Nested.fromDict(Map<string, dynamic> dict){
        this.a = dict["a"]
        
    }
}

class TestIn{
    TestIn(, inta, Stringb, boolc, doubled, Mape, Listf, dynamicg, {int aO=null, String bO=null, bool cO=null, double dO=null, Map eO=null, List fO=null, dynamic gO=null, }){
        this.a = a;
        this.a_o = aO;
        this.b = b;
        this.b_o = bO;
        this.c = c;
        this.c_o = cO;
        this.d = d;
        this.d_o = dO;
        this.e = e;
        this.e_o = eO;
        this.f = f;
        this.f_o = fO;
        this.g = g;
        this.g_o = gO;
        
    }

    Map<string, dynamic> toDict(){
        Map<string, dynamic> dict;
        dict["a"] = this.a;
        dict["a_o"] = this.a_o;
        dict["b"] = this.b;
        dict["b_o"] = this.b_o;
        dict["c"] = this.c;
        dict["c_o"] = this.c_o;
        dict["d"] = this.d;
        dict["d_o"] = this.d_o;
        dict["e"] = this.e;
        dict["e_o"] = this.e_o;
        dict["f"] = this.f;
        dict["f_o"] = this.f_o;
        dict["g"] = this.g;
        dict["g_o"] = this.g_o;
        
        return dict;
    }

    TestIn.fromDict(Map<string, dynamic> dict){
        this.a = dict["a"]
        this.a_o = dict["a_o"]
        this.b = dict["b"]
        this.b_o = dict["b_o"]
        this.c = dict["c"]
        this.c_o = dict["c_o"]
        this.d = dict["d"]
        this.d_o = dict["d_o"]
        this.e = dict["e"]
        this.e_o = dict["e_o"]
        this.f = dict["f"]
        this.f_o = dict["f_o"]
        this.g = dict["g"]
        this.g_o = dict["g_o"]
        
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
