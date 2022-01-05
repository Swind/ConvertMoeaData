import fire
import moea_data_downloader as MoeaDataDownloader
import sectname as SectName

class CLI:
    def download_moea_data(self):
        """從經濟部下載資料到 moea_data 資料夾"""
        MoeaDataDownloader.download()
        pass

    def download_metadata(self):
        """從經濟部開放資料下載城市、鄉鎮與地段號的代碼"""
        SectName.download_county_list()
        SectName.download_town_list()

    def query_sectcode(self, address):
        """輸入地址例如: 新莊區海山頭段石龜小段82號之18,查詢地段號
        """
        full_list, simple_list = SectName.convert_address_to_sectcode(address)
        for item in full_list:
            print(item)

        for item in simple_list:
            print(item)


if __name__ == "__main__":
    fire.Fire(CLI)
