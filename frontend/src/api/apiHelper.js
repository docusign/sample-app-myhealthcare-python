export async function handleResponse(response) {
  if (response.status === 200) {
    return response;
  }
  if (response.status === 400) {
    const error = await response.text();
    throw new Error(error);
  }
  throw new Error(response);
}

export function handleError(error, setShowModal=undefined) {
  if (error.response && error.response.status === 402) {
    setShowModal(true);
  }
  console.error("API call failed. " + JSON.stringify(error));
  throw error;
}