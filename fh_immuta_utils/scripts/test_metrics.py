from fh_immuta_utils.metrics import test_metrics
import click


@click.command(help="Sending test metrics to datadog")
def cli_entrypoint():
    return main()


def main():
    print("sending test metrics to datadog...")
    test_metrics()
    return 0


if __name__ == "__main__":
    cli_entrypoint()
