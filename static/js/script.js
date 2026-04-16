const buttonMoreOptions = document.getElementById('moreOptions')
const navBar = document.getElementById('navBar')
const navList = document.getElementById('navList')

buttonMoreOptions.addEventListener('click', () => {
    if (navList.style.display === 'none') {
        navList.style.display = 'flex'
        navBar.style.backgroundColor = '#21282e'
    } else {
        navList.style.display = 'none'
        navBar.style.backgroundColor = 'transparent'
    }
    
})

const buttonSign = document.getElementById('buttonInscrever')
const formEmail = document.getElementById('formEmail')
const inputEmail = document.getElementById('inputEmail')

buttonSign.addEventListener('click', () => {
    inputEmail.focus()
    requestAnimationFrame(
        formEmail.scrollIntoView({behavior:"smooth", block:"center"})
    )

})

const linkConhecimento = document.getElementById('linkConhecimento')
const layoutConhecimento = document.getElementById('conhecimento')

const linkDepoimento = document.getElementById('linkDepoimento')
const layoutDepoimento = document.getElementById('depoimento')

linkConhecimento.addEventListener('click', () => {
    requestAnimationFrame(
        layoutConhecimento.scrollIntoView({behavior:'smooth', block:'center'})
    )
})
linkDepoimento.addEventListener('click', () => {
    requestAnimationFrame(
        layoutDepoimento.scrollIntoView({behavior:'smooth', block:'center'})
    )
})