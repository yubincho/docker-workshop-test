


# Terraform Demo (GCP)

- Module 1에서 Terraform을 사용해 **GCP 리소스를 생성/관리**하는 실습을 진행했습니다.  
(Zoomcamp 강의 내용 기반 + 실습 과정 정리)
- 추가 업데이트 예정 📄

<br><br>

## ✅ What I did
- GCP Service Account Key(JSON) 생성 및 인증 설정
- Terraform Provider 설정
- `terraform init → plan → apply` 흐름 실습
- 필요 시 리소스 삭제(`destroy`)까지 수행
- 추가 업데이트 예정 📄


<br><br>

## ◼️ Authentication (GCP)

### Option 1) Environment Variable 방식 
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/workspaces/docker-workshop-test/module1/terrademo/keys/my-creds.json"
```
<br>

- 확인
```
echo $GOOGLE_APPLICATION_CREDENTIALS
ls -l $GOOGLE_APPLICATION_CREDENTIALS
```

<br>

### Option 2) Terraform provider에 직접 지정

main.tf
```
provider "google" {
  credentials = "./keys/my-creds.json"
}
```

<br><br>

## ◼️ Terraform Commands
1) Format
```
terraform fmt -recursive
```

<br>

2) Init
```
terraform init
```

<br>

3) Plan
```
terraform plan
```

<br>

4) Apply
```
terraform apply
```

<br>

5) Destroy (리소스 삭제)
```
terraform destroy
```

<br><br>

## ◼️ Notes

- credentials 오타(credentails)로 인해 plan이 실패해서
Terraform 에러 메시지를 보고 빠르게 수정했습니다.
- Codespaces 환경에서는 Terraform CLI가 설치되어 있어야 명령이 동작합니다.
- **.gitignore 예시**  
   - `keys/*.json` 절대 올라가지 않게 ***.json** 을 추가함
- **만들었던 리소스 목록**  
   - 예: bucket / IAM / service account 


<br><br>
