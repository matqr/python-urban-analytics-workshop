from huggingface_hub import HfApi, hf_hub_download


def download_folder(repo_id, repo_type, folder_path, local_dir):
    """
    Download an entire folder from a huggingface dataset repository.

    repo_id : string
        The ID of the repository (e.g., 'username/repo_name').
    repo_type : string
        Type of the repo, dataset or model.
    folder_path : string
        The path to the folder within the repository.
    local_dir : string
        Local folder to download the data. This mimics git behaviour
    """
    api = HfApi()
    # list all files in the repo, keep the ones within folder_path
    all_files = api.list_repo_files(repo_id, repo_type=repo_type)
    files_list = [f for f in all_files if f.startswith(folder_path)]

    # download each of those files
    for file_path in files_list:
        hf_hub_download(repo_id=repo_id, repo_type=repo_type,
                        filename=file_path, local_dir=local_dir)


# Download entire data/ folder
repo_id = "NUS-UAL/global-streetscapes"
repo_type = "dataset"
folder_path = "data/"
local_dir = "global-streetscapes/"

# By degfault, huggingface download them to the .cache/huggingface folder
download_folder(repo_id, repo_type, folder_path, local_dir)

# Download 2 additional files
hf_hub_download(repo_id=repo_id, repo_type=repo_type,
                filename="cities688.csv", local_dir=local_dir)
hf_hub_download(repo_id=repo_id, repo_type=repo_type,
                filename="info.csv", local_dir=local_dir)
