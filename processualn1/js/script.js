/* BANCO DE DADOS DA COLEÇÃO */
const produtos = {
    "oud-imperial": {
        nome: "Oud Imperial",
        descricao: "Uma fragrância imponente com notas de madeira nobre, âmbar e especiarias orientais. Criado para quem deseja marcar presença com sofisticação e mistério.",
        preco: "R$ 450,00",
        imagem: "../images/oldimperial.png"
    },
    "nectar-dor": {
        nome: "Nectar d'Or",
        descricao: "A doçura do mel silvestre combinada com a sofisticação da baunilha e flores brancas. Uma aura dourada que envolve os sentidos em puro luxo.",
        preco: "R$ 389,00",
        imagem: "../images/nectardor.png"
    },
    "brisa-de-capri": {
        nome: "Brisa de Capri",
        descricao: "Limão siciliano e notas marinhas refrescantes. Uma fragrância leve que transporta você diretamente para uma tarde ensolarada na costa italiana.",
        preco: "R$ 320,00",
        imagem: "../images/brisadecapri.png"
    },
    "velvet-rose": {
        nome: "Velvet Rose",
        descricao: "Pétalas de rosas damascenas e musk aveludado. Uma experiência romântica, delicada e extremamente elegante para momentos especiais.",
        preco: "R$ 395,00",
        imagem: "../images/velvelrose.png"
    },
    "noite-versalhes": {
        nome: "Noite Versalhes",
        descricao: "Patchouli intenso com toque de chocolate amargo. Uma fragrância noturna, profunda e sedutora, inspirada nos bailes da realeza.",
        preco: "R$ 510,00",
        imagem: "../images/noiteversalhes.png"
    },
    "santal-silk": {
        nome: "Santal Silk",
        descricao: "Sândalo cremoso com sutil aroma de cardamomo. O equilíbrio perfeito entre o conforto e o luxo minimalista em uma essência única.",
        preco: "R$ 415,00",
        imagem: "../images/saltalsilk.png"
    },
    "bloom-aura": {
        nome: "Bloom Aura",
        descricao: "Um buquê explosivo de jasmim, lírio e gardênia. A celebração da feminilidade em uma aura floral radiante e inesquecível.",
        preco: "R$ 340,00",
        imagem: "../images/bloomaura.png"
    },
    "ebano-noir": {
        nome: "Ébano Noir",
        descricao: "Couro sofisticado com fundo de incenso defumado. Uma fragrância densa e marcante para personalidades fortes e decididas.",
        preco: "R$ 480,00",
        imagem: "../images/ebanonoir.png"
    }
};

/* LÓGICA DE CAPTURA E PREENCHIMENTO */

// 1. Captura o ID que vem na URL (ex: ?id=oud-imperial)
const urlParams = new URLSearchParams(window.location.search);
const idProduto = urlParams.get('id');

// 2. Mapeamento dos novos IDs do seu HTML
const imgElement = document.getElementById('foto-produto');
const nomeElement = document.getElementById('produto-nome');
const descElement = document.getElementById('descricao');
const precoElement = document.getElementById('produto-preco');

// 3. Verifica se o produto existe e preenche a página
if (idProduto && produtos[idProduto]) {
    const p = produtos[idProduto];

    nomeElement.innerText = p.nome;
    descElement.innerText = p.descricao;
    precoElement.innerText = p.preco;
    imgElement.src = p.imagem;
    imgElement.alt = `Frasco do perfume ${p.nome}`;

    // Altera o título da aba para o nome do perfume
    document.title = `${p.nome} | Sinta-Se`;
} else {
    // Caso ocorra erro ou ID não encontrado
    if (nomeElement) {
        nomeElement.innerText = "Produto não encontrado";
        descElement.innerText = "Por favor, selecione um perfume válido em nossa coleção.";
    }
}