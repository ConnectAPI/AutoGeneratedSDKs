// Auto generated file, DO NOT EDIT!




class BodyFileOptional{
    constructor(a=null, ){
        this.a = a
        
    }
    
    static from_dict(dict){
        return new BodyFileOptional(dict["a"],);
    }
}

class BodyFile{
    constructor(a,){
        this.a = a
        
    }
    
    static from_dict(dict){
        return new BodyFile(dict["a"],);
    }
}

class BodyFormOptional{
    constructor(a=null, ){
        this.a = a
        
    }
    
    static from_dict(dict){
        return new BodyFormOptional(dict["a"],);
    }
}

class BodyForm{
    constructor(a,){
        this.a = a
        
    }
    
    static from_dict(dict){
        return new BodyForm(dict["a"],);
    }
}

class HTTPValidationError{
    constructor(detail=null, ){
        this.detail = detail
        
    }
    
    static from_dict(dict){
        return new HTTPValidationError(dict["detail"],);
    }
}

class Nested{
    constructor(a=null, ){
        this.a = a
        
    }
    
    static from_dict(dict){
        return new Nested(dict["a"],);
    }
}

class TestIn{
    constructor(a,b,c,d,e,f,g,a_o=null, b_o=null, c_o=null, d_o=null, e_o=null, f_o=null, g_o=null, ){
        this.a = a
        this.a_o = a_o
        this.b = b
        this.b_o = b_o
        this.c = c
        this.c_o = c_o
        this.d = d
        this.d_o = d_o
        this.e = e
        this.e_o = e_o
        this.f = f
        this.f_o = f_o
        this.g = g
        this.g_o = g_o
        
    }
    
    static from_dict(dict){
        return new TestIn(dict["a"],dict["a_o"],dict["b"],dict["b_o"],dict["c"],dict["c_o"],dict["d"],dict["d_o"],dict["e"],dict["e_o"],dict["f"],dict["f_o"],dict["g"],dict["g_o"],);
    }
}

class ValidationError{
    constructor(loc,msg,type,){
        this.loc = loc
        this.msg = msg
        this.type = type
        
    }
    
    static from_dict(dict){
        return new ValidationError(dict["loc"],dict["msg"],dict["type"],);
    }
}


export {BodyFileOptional, BodyFile, BodyFormOptional, BodyForm, HTTPValidationError, Nested, TestIn, ValidationError, };