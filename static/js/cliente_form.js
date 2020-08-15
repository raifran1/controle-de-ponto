function iniciar_atendimento(){
    
    btn_iniciar = document.getElementById('btn-iniciar')
    btn_iniciar.style.background = "black" 

    btn_consultar = document.getElementById('btn-consultar')
    btn_consultar.style.display = "none" 
    
    colaborador = document.getElementById('div_colaborador')
    colaborador.style.display = "block" 

    empresa = document.getElementById('div_empresa')
    empresa.style.display = "block" 

    tipo_atendimento = document.getElementById('div_tipo_atendimento')
    tipo_atendimento.style.display = "block"

    cadastrar = document.getElementById('myForm')
    cadastrar.style.display = "block"
    
}
    
function consultar_atendimento(){
    btn_consultar = document.getElementById('btn-consultar')    
    btn_consultar.style.background = "black" 

    btn_iniciar = document.getElementById('btn-iniciar')
    btn_iniciar.style.display = "none" 

    // rodape = document.getElementById('rodape')
    // rodape.style.display = "block" 
    
    inserir_token = document.getElementById('consultar_atendimento');
    inserir_token.style.display = 'block';
  
}


function onchange_tipo_atendimento(valor) {
    if (valor != ''){
        document.getElementById('div_assunto').style.display = "block"
        document.getElementById('div_descricao').style.display = "none"
        document.getElementById('box_rating').style.display = "none"
           
    }else{
        document.getElementById('div_assunto').style.display = "none"
        document.getElementById('div_descricao').style.display = "none"
        document.getElementById('submit_atendimento').style.display = "none"
        document.getElementById('box_rating').style.display = "none"
    }
}

function onchange_assunto(valor) {
    if (valor != ''){
        document.getElementById('div_descricao').style.display = "block"
        document.getElementById('submit_atendimento').style.display = "block"

        id_tipo =  document.getElementById('id_type_service').value
        if ((valor == "1") || (valor == "3")){
            document.getElementById('box_rating').style.display = "block"
        }else{
            document.getElementById('box_rating').style.display = "none"
        }

    }else{
        document.getElementById('div_descricao').style.display = "none"
        document.getElementById('submit_atendimento').style.display = "none"
        document.getElementById('box_rating').style.display = "none"
    }
}


const stars = document.querySelector('.ratings').children;

let index

for (let i=0; i<stars.length; i++){
    stars[i].addEventListener("mouseover", function(){
        for(let j=0; j<stars.length; j++){
            stars[j].classList.remove("fa-star")
            stars[j].classList.add("fa-star-o")
        }
        for(let j=0; j<=i; j++){
            stars[j].classList.remove("fa-star-o")
            stars[j].classList.add("fa-star")
        }
    })

    stars[i].addEventListener("click", function(){
        console.log(i+1)
        document.getElementById('id_avaliacao').value = i+1
        index = i
    })
    stars[i].addEventListener("mouseout", function(){
        for(let j=0; j<stars.length; j++){
            stars[j].classList.remove("fa-star")
            stars[j].classList.add("fa-star-o")
        }
        for(let j=0; j<=index; j++){
            stars[j].classList.remove("fa-star-o")
            stars[j].classList.add("fa-star")
        }
    })      
}

function contato() {
    document.getElementById('div_colaborador').style.display = "block"
    document.getElementById('div_empresa').style.display = "block"
}
document.getElementById('id_description').rows = 4
