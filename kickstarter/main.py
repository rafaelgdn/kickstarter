from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from bs4 import BeautifulSoup
import asyncio
import csv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir_abspath = os.path.abspath(current_dir)


async def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")  # uncomment this line to run in headless mode
    # options.add_argument("--disable-gpu")  # comment to run in a cloud
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
    options.add_argument("--disable-features=OutOfBlinkCors")
    options.add_argument("--disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure")
    options.add_argument("--disable-features=CrossSiteDocumentBlockingIfIsolating,CrossSiteDocumentBlockingAlways")
    options.add_argument("--disable-features=ImprovedCookieControls,LaxSameSiteCookies,SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure")
    options.add_argument("--disable-features=SameSiteDefaultChecksMethodRigorously")
    driver = await webdriver.Chrome(options=options)
    return driver


def clean_for_csv(text):
    if isinstance(text, str):
        return text.replace("\n", " ").replace("\r", "").replace('"', '""')
    return text


def read_creators_urls():
    urls = []
    csv_path = os.path.join(current_dir, "creators_urls.csv")
    with open(csv_path, "r") as file:
        for line in file:
            url = line.strip()
            if url:
                urls.append(url)
    return urls


def save_creators_in_file(users):
    creator_data_path = f"{current_dir_abspath}/creators.csv"
    creator_data_path_exists = os.path.exists(creator_data_path)
    creator_data_file_empty = creator_data_path_exists and os.path.getsize(creator_data_path) == 0

    with open(creator_data_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=users[0].keys(), quoting=csv.QUOTE_ALL)
        if not creator_data_path_exists or creator_data_file_empty:
            writer.writeheader()
        cleaned_users = [{k: clean_for_csv(v) for k, v in user.items()} for user in users]
        writer.writerows(cleaned_users)


def save_errors(url):
    errors_path = f"{current_dir_abspath}/errors.csv"
    with open(errors_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([url])


async def main():
    driver = await start_driver()
    urls = read_creators_urls()

    for url in urls:
        try:
            await driver.get(url, wait_load=True)
            await driver.sleep(0.5)
            about_button = await driver.find_element(By.ID, "profile_about")
            await about_button.click()
            await driver.sleep(2)

            creator = {
                "creatorUrl": url,
                "creatorName": "",
                "creatorLocation": "",
                "creatorCountry": "",
                "creatorState": "",
                "creatorCity": "",
                "creatorJoined": "",
                "creatorBackerFavorite": "",
                "creatorSuperbacker": "",
                "creatorAbout": "",
                "creatorWebsite01": "",
                "creatorWebsite02": "",
                "creatorWebsite03": "",
                "creatorWebsite04": "",
                "creatorWebsite05": "",
                "creatorBacked": "",
                "creatorCreated": "",
                "creatorProject01": "",
                "creatorProject02": "",
                "creatorProject03": "",
                "creatorProject04": "",
                "creatorProject05": "",
                "creatorProject06": "",
                "creatorProject07": "",
                "creatorProject08": "",
                "creatorProject09": "",
                "creatorProject10": "",
                "creatorProject11": "",
                "creatorProject12": "",
                "creatorProject13": "",
                "creatorProject14": "",
                "creatorProject15": "",
                "creatorProject16": "",
                "creatorProject17": "",
                "creatorProject18": "",
                "creatorProject19": "",
                "creatorProject20": "",
                "creatorProject21": "",
                "creatorProject22": "",
                "creatorProject23": "",
                "creatorProject24": "",
                "creatorProject25": "",
                "creatorProject26": "",
                "creatorProject27": "",
                "creatorProject28": "",
                "creatorProject29": "",
                "creatorProject30": "",
                "creatorProject31": "",
                "creatorProject32": "",
                "creatorProject33": "",
                "creatorProject34": "",
                "creatorProject35": "",
                "creatorProject36": "",
                "creatorProject37": "",
                "creatorProject38": "",
                "creatorProject39": "",
                "creatorProject40": "",
                "creatorProject41": "",
                "creatorProject42": "",
                "creatorProject43": "",
                "creatorProject44": "",
                "creatorProject45": "",
                "creatorProject46": "",
                "creatorProject47": "",
                "creatorProject48": "",
                "creatorProject49": "",
                "creatorProject50": "",
                "creatorProject51": "",
                "creatorProject52": "",
                "creatorProject53": "",
                "creatorProject54": "",
                "creatorProject55": "",
                "creatorProject56": "",
                "creatorProject57": "",
                "creatorProject58": "",
                "creatorProject59": "",
                "creatorProject60": "",
                "creatorProject61": "",
                "creatorProject62": "",
                "creatorProject63": "",
                "creatorProject64": "",
                "creatorProject65": "",
                "creatorProject66": "",
                "creatorProject67": "",
                "creatorProject68": "",
                "creatorProject69": "",
                "creatorProject70": "",
                "creatorProject71": "",
                "creatorProject72": "",
                "creatorProject73": "",
                "creatorProject74": "",
                "creatorProject75": "",
                "creatorProject76": "",
                "creatorProject77": "",
                "creatorProject78": "",
                "creatorProject79": "",
                "creatorProject80": "",
                "creatorProject81": "",
                "creatorProject82": "",
                "creatorProject83": "",
                "creatorProject84": "",
                "creatorProject85": "",
                "creatorProject86": "",
                "creatorProject87": "",
                "creatorProject88": "",
                "creatorProject89": "",
                "creatorProject90": "",
                "creatorProject91": "",
                "creatorProject92": "",
                "creatorProject93": "",
                "creatorProject94": "",
                "creatorProject95": "",
                "creatorProject96": "",
                "creatorProject97": "",
                "creatorProject98": "",
                "creatorProject99": "",
                "creatorProject100": "",
            }

            content = await driver.page_source
            soup = BeautifulSoup(content, "html.parser")

            name_element = soup.css.select("div.profile_bio a[href*='/profile/']")
            if name_element:
                creator["creatorName"] = soup.css.select("div.profile_bio a[href*='/profile/']")[0].text.strip()
            else:
                creator["creatorName"] = ""

            location_element = soup.css.select("div.profile_bio span.location a")
            if location_element:
                creator["creatorLocation"] = soup.css.select("div.profile_bio span.location a")[0].text.strip()
                # creator["creatorState"] = soup.css.select("div.profile_bio span.location a")[0].text.split(",")[1].strip()
                # creator["creatorCity"] = soup.css.select("div.profile_bio span.location a")[0].text.split(",")[0].strip()
            else:
                creator["creatorLocation"] = ""
                # creator["creatorState"] = ""
                # creator["creatorCity"] = ""

            joined_element = soup.css.select("div.profile_bio span.joined time")
            if joined_element:
                creator["creatorJoined"] = soup.css.select("div.profile_bio span.joined time")[0].text.strip()
            else:
                creator["creatorJoined"] = ""

            badges_element = soup.css.select("#react-profile-badges")
            if badges_element:
                creator["creatorBackerFavorite"] = True if "backer-favorite" in soup.css.select("#react-profile-badges")[0]["data-badges"] else False
                creator["creatorSuperbacker"] = True if "superbacker" in soup.css.select("#react-profile-badges")[0]["data-badges"] else False
            else:
                creator["creatorBackerFavorite"] = False
                creator["creatorSuperbacker"] = False

            about_element = soup.css.select("#content > div > div > div p + p")
            if about_element:
                creator["creatorAbout"] = soup.css.select("#content > div > div > div p + p")[0].text.strip()
            else:
                creator["creatorAbout"] = ""

            backed_element = soup.css.select("#profile_backed span.count")
            if backed_element:
                creator["creatorBacked"] = soup.css.select("#profile_backed span.count")[0].text.strip()
            else:
                creator["creatorBacked"] = 0

            created_element = soup.css.select("#profile_created span.count")
            if created_element:
                creator["creatorCreated"] = soup.css.select("#profile_created span.count")[0].text.strip()
            else:
                creator["creatorCreated"] = 0

            websites = soup.css.select("ul.menu-submenu a")
            if websites:
                for i, website in enumerate(websites):
                    creator[f"creatorWebsite0{i+1}"] = website["href"]

            created_button = await driver.find_element(By.ID, "profile_created")
            await created_button.click()
            await driver.sleep(5)

            has_next_button = True
            project_index = 0

            while has_next_button:
                created_content = await driver.page_source
                created_soup = BeautifulSoup(created_content, "html.parser")
                projects = created_soup.css.select("#content a[href*='/projects/']")
                unique_projects = list({project["href"]: project for project in projects}.values())
                if not unique_projects:
                    break

                for i, project in enumerate(unique_projects):
                    project_index += 1

                    if project_index < 10:
                        creator[f"creatorProject0{project_index}"] = project["href"]
                    else:
                        creator[f"creatorProject{project_index}"] = project["href"]

                try:
                    next_button = await driver.find_element(By.CSS_SELECTOR, "div[role='navigation'] .next_page")
                    next_button_tag = await next_button.tag_name
                    if next_button_tag == "span":
                        has_next_button = False
                        break
                    await next_button.click()
                    await driver.sleep(5)
                except Exception:
                    has_next_button = False

            print(f"Creator for url: {url} was saved successfully")
            save_creators_in_file([creator])
        except Exception as e:
            print(f"Error processing URL {url}: {str(e)}")
            save_errors(url)
            await driver.quit()
            driver = await start_driver()

    await driver.quit()


asyncio.run(main())
