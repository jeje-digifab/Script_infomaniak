#!/usr/bin/env python3

class InfoManiHack:
    """
    Class to handle InfoManiHack operations.
    """

    def txt_record(self):
        """
        Function to fetch TXT records for a given URL.
        """
        import dns.resolver
        import re

        url = 'candiharvest.infomanihack.ch'

        try:
            result = dns.resolver.resolve(url, 'TXT')

            for val in result:
                id_txt = val.to_text()
                id_txt = re.sub(r'"', '', id_txt)
                print(id_txt)
                return id_txt
        except Exception as e:
            print(f"Error fetching TXT record: {e}")
            return None

    def header(self):
        """
        Function to fetch headers from a URL using urllib3.
        """
        import urllib3

        try:
            candidate_id = self.txt_record()

            if candidate_id is None:
                print("No candidate ID retrieved, aborting header request.")
                return None

            resp = urllib3.request(
                "GET",
                "https://candiharvest.infomanihack.ch",
                headers={"X-Candidate-Id": candidate_id},
            )

            result = resp.data.decode("utf-8")
            return result

        except Exception as e:
            print(f"Error fetching header: {e}")
            return None


if __name__ == "__main__":
    app = InfoManiHack()
    output = app.header()
    print("Final output:")
    print(output)
