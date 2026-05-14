import time

EMPRESA = {
    "Matriz": {
        "TI": {
            "Infraestrutura": {
                "Servidores": 120_000,
                "Redes":       45_000,
                "Seguranca":   30_000,
            },
            "Desenvolvimento": {
                "Backend":  95_000,
                "Frontend": 78_000,
                "QA":       42_000,
            },
            "Suporte": 28_000,
        },
        "RH": {
            "Recrutamento": 61_000,
            "Treinamento": {
                "Capacitacao":  23_000,
            },
            "Beneficios": 55_000,
        },
        "Financeiro": {
            "Contabilidade":     47_000,
            "Auditoria_Interna": 38_000,
            "Tesouraria":        66_000,
        },
        "Marketing": {
            "Digital": {
                "Midia_Paga": 82_000,
            },
            "Eventos": 34_000,
            "Criacao": 29_000,
        },
    },
    "Filial_SP": {
        "Operacoes": {
            "Logistica": 91_000,
            "Estoque":   53_000,
        },
        "Vendas": {
            "Inside_Sales": 58_000,
            "Field_Sales":  20_000,
            "Pre_Venda":    31_000,
        },
        "Administrativo": 26_000,
    },
    "Filial_RJ": {
        "Operacoes": {
            "Logistica":  49_000,
            "Manutencao": 22_000,
        },
        "Vendas": {
            "Varejo":      67_000,
            "Corporativo": 88_000,
        },
    },
}


def _percorrer(no, excluidos):
    if isinstance(no, (int, float)):
        return no
    return sum(
        _percorrer(filho, excluidos)
        for chave, filho in no.items()
        if chave not in excluidos
    )


def auditor(fn):
    def wrapper(*args, **kwargs):
        linha = "─" * 54

        depto_ignorados = [a for a in args[1:] if isinstance(a, str)]
        moeda = kwargs.get("moeda_destino", "USD")
        taxa  = kwargs.get("taxa_cambio", 1.0)

        print(f"\n╔{linha}╗")
        print(f"║{'AUDITORIA FINANCEIRA':^54}║")
        print(f"╠{linha}╣")
        print(f"║  Função        : {fn.__name__:<36}║")
        print(f"║  Moeda destino : {moeda:<36}║")
        print(f"║  Taxa de câmbio: {taxa:<36}║")

        if depto_ignorados:
            ignorados_fmt = ", ".join(depto_ignorados)
            print(f"║  Ignorados     : {ignorados_fmt:<36}║")
        else:
            print(f"║  Ignorados     : {'Nenhum':<36}║")

        print(f"╠{linha}╣")

        t0 = time.perf_counter()
        resultado = fn(*args, **kwargs)
        elapsed = time.perf_counter() - t0

        print(f"╠{linha}╣")
        print(f"║  Tempo         : {elapsed:.6f}s{'':<27}║")
        print(f"╚{linha}╝\n")

        return resultado

    wrapper.__name__ = fn.__name__
    return wrapper


@auditor
def calcular_orcamento(estrutura, *args, **kwargs):
    """
    Soma os orçamentos de toda a hierarquia, com suporte a exclusões e conversão cambial.

    Args:
        estrutura (dict): árvore de departamentos exportada pelo financeiro.
        *args (str):      nomes de departamentos a desconsiderar (e seus filhos).
        **kwargs:
            moeda_destino (str):   código da moeda de saída. Padrão: "USD".
            taxa_cambio   (float): multiplicador aplicado ao total. Padrão: 1.0.

    Returns:
        float: total convertido na moeda destino.
    """
    taxa  = kwargs.get("taxa_cambio", 1.0)
    moeda = kwargs.get("moeda_destino", "USD")

    total_base = _percorrer(estrutura, excluidos=set(args))
    total_convertido = total_base * taxa

    simbolo = "R$" if moeda == "BRL" else moeda
    print(f"  Base (USD)   : $ {total_base:>14,.2f}")
    print(f"  Convertido   : {simbolo} {total_convertido:>13,.2f}  [{moeda}]")

    return total_convertido


if __name__ == "__main__":

    print("\n>>> Orçamento consolidado (sem filtros)\n")
    calcular_orcamento(EMPRESA)

    print(">>> Excluindo Marketing e Filial_RJ — conversão para BRL\n")
    calcular_orcamento(
        EMPRESA,
        "Marketing", "Filial_RJ",
        moeda_destino="BRL",
        taxa_cambio=5.25,
    )

    print(">>> Excluindo TI e Vendas — conversão para EUR\n")
    calcular_orcamento(
        EMPRESA,
        "TI", "Vendas",
        moeda_destino="EUR",
        taxa_cambio=0.93,
    )
