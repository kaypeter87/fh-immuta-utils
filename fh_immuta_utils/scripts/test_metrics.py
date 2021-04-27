from fh_immuta_utils.metrics import test_metrics


def cli_entrypoint():
    main()


def main():
    print("sending test metrics to datadog...")
    test_metrics()


if __name__ == "__main__":
    cli_entrypoint()
